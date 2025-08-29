import random
import time
from sqlalchemy.orm import sessionmaker
from engine import engine
from tables import Player,Board
from cards import draw_chance_card, draw_community_chest_card
from property import handle_player_landing, buy_property

from rich import print
from rich.console import Console
from rich.prompt import Prompt

Session = sessionmaker(bind=engine)
session = Session()
console = Console()

class Dice:
    def __init__(self):
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        self.roll = self.dice1 + self.dice2

    def is_double(self):
        return self.dice1 == self.dice2

class Game:
    def __init__(self):
        self.players = []
        self.jail_turns = {} 
        self.resume()
        if not self.players:
            self.get_players()

    def resume(self):
        existing_players = session.query(Player).all()
        while True:
            if existing_players:
                console.print("-----------------------------------------")
                console.print("[bold red]WELCOME TO MONOPOLY![/bold red]")
                console.print("-----------------------------------------")
                console.print("[bold magenta]An existing game was found.[/bold magenta]")
                choice = Prompt.ask("[bold cyan]Do you want to continue?[/] (y/n)").strip().lower()
                if choice == "y":
                    console.print("[green]Resuming existing game[/green]")
                    console.print(" ")
                    self.players = existing_players
                    # Initialize jail_turns
                    for player in self.players:
                        self.jail_turns[player.name] = 0
                    return
                elif choice == "n":
                    console.print("[yellow]Starting a new game[/yellow]")
                    for player in existing_players:
                        session.delete(player)
                    session.commit()
                    return
                else:
                    console.print("[red]Wrong input, please try again.[/red]")
            else:
                return

    def get_players(self):
        while True:
            number_input = Prompt.ask("[bold cyan]How many players will be playing?[/]")
            if number_input.isdigit():
                number = int(number_input)
                if number < 2:
                    console.print("[red]Minimum number of players is 2.[/red]")
                elif number > 8:
                    console.print("[red]Maximum number of players is 8.[/red]")
                else:
                    break
            else:
                console.print("[red]Please enter a valid number.[/red]")

        for i in range(number):
            while True:
                name = Prompt.ask(f"[bold magenta]Enter player name {i+1}[/]").strip()
                console.print(" ")
                if name.isalpha():
                    new_player = Player(name=name, money=1500, in_jail=False)
                    session.add(new_player)
                    session.commit()
                    self.players.append(new_player)
                    self.jail_turns[name] = 0  # Initialize jail turns here
                    break
                else:
                    console.print("[red]Name must contain only letters (no digits, spaces, or symbols).[/red]")

    def play(self):
        duration = 6000
        Start = time.time()

        while True:
            Stop = time.time() - Start
            if Stop >= duration:
                console.print("[bold red]Time's up! Game over.[/bold red]")
                return

            for player in self.players:
                player_obj = session.query(Player).filter_by(name=player.name).first()

                if player_obj.in_jail:
                    self.jail_turns[player.name] += 1
                    turn_count = self.jail_turns[player.name]
                    console.print(f"[bold red]{player.name} is in jail.")

                    if turn_count >= 1:
                        console.print(f"[green]{player.name} has served their time and is released from jail![/green]")
                        player_obj.in_jail = False
                        self.jail_turns[player.name] = 0
                    else:
                        session.commit()
                        continue

                rolling = True
                while rolling:
                    Stop = time.time() - Start
                    if Stop >= duration:
                        console.print("[bold red]Time's up! Game over.[/bold red]")
                        return

                    choice = Prompt.ask(f"[bold green]{player.name}[/], do you want to roll the dice? (y/n)").lower()
                    if choice == "y":
                        dice = Dice()
                        console.print(f":game_die: [bold green]{player.name} rolled: {dice.dice1} + {dice.dice2} = {dice.roll}[/bold green]")
                        starting_position = player_obj.position
                        new_position = starting_position + dice.roll
                        final_position = new_position % 40

                        if final_position < starting_position:
                            player_obj.money += 200
                            player_obj.laps = (player_obj.laps or 0) + 1
                            console.print(f":moneybag: [yellow]{player_obj.name} passed GO! +$200. New Balance: ${player_obj.money}[/yellow]")

                        player_obj.position = final_position

                        board_space = session.query(Board).filter_by(position=final_position).first()
                        if board_space:
                            console.print(f":round_pushpin: [blue]{player.name} landed on: {board_space.name}[/blue]")

                        if final_position in [7, 22, 36]:
                            draw_chance_card(player_obj.name)
                        elif final_position in [2, 17, 33]:
                            draw_community_chest_card(player_obj.name)

                        if final_position == 30:
                            console.print("[bold red]You landed on 'Go to Jail'! Pay $50 or go to jail.[/bold red]")
                            while True:
                                jail_choice = Prompt.ask("[bold]Do you want to pay $50?[/] (y/n)").strip().lower()
                                if jail_choice == "y":
                                    if player_obj.money >= 50:
                                        player_obj.money -= 50
                                        console.print(f"[green]$50 deducted. You're free to go! New balance: ${player_obj.money}[/green]")
                                    else:
                                        console.print("[red]Insufficient funds. You are sent to jail.[/red]")
                                        player_obj.position = 10
                                        player_obj.in_jail = True
                                        self.jail_turns[player.name] = 0
                                        rolling = False
                                    session.commit()
                                    break
                                elif jail_choice == "n":
                                    console.print("[red]You chose not to pay. Going to jail.[/red]")
                                    player_obj.position = 10
                                    player_obj.in_jail = True
                                    self.jail_turns[player.name] = 0
                                    rolling = False
                                    session.commit()
                                    break
                                else:
                                    console.print("[red]Invalid input. Please try again.[/red]")

                        result = handle_player_landing(player_obj)
                        if result == "bankrupt":
                            console.print(f"[bold red]{player_obj.name} can't pay rent and is out of the game![/bold red]")
                            session.delete(player_obj)
                            session.commit()
                            self.players = [p for p in self.players if p.id != player_obj.id]
                            rolling = False
                            break

                        elif result is not None:
                            prop = result
                            buy_choice = Prompt.ask(f"{player_obj.name}, do you want to buy {prop.name} for ${prop.price}? (y/n)").lower()
                            if buy_choice == "y":
                                if buy_property(session, player_obj, prop):
                                    console.print(f"[green]{player_obj.name} bought {prop.name}![/green]")
                                else:
                                    console.print(f"[red]Not enough money to buy {prop.name}.[/red]")

                        session.commit()
                        console.print(f":arrow_right: [cyan]{player.name} is now at position {player_obj.position}[/cyan]")
                        console.print("----------------------------------------------------------------------------------")
                        console.print("  ")

                        if dice.is_double():
                            console.print("[yellow]Double rolled! You get another turn.[/yellow]")
                            continue
                        else:
                            rolling = False

                    elif choice == "n":
                        console.print("[red]You must roll the dice to continue playing.[/red]")
                    else:
                        console.print("[red]Invalid choice. Enter 'y' or 'n'.[/red]")

if __name__ == "__main__":
    game = Game()
    game.play()
