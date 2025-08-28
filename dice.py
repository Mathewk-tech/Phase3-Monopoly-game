import random
import time
from sqlalchemy.orm import sessionmaker
from engine import engine
from tables import Player, Board
from cards import draw_chance_card, draw_community_chest_card

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
        self.resume()
        if not self.players:
            self.get_players()

    def resume(self):
        existing_players = session.query(Player).all()
        while True:
            if existing_players:
                choice = Prompt.ask("[bold cyan]Do you want to continue?[/] (y/n)").strip().lower()
                if choice == "y":
                    console.print("[green]Resuming existing game[/green]")
                    self.players = existing_players
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
                if name.isalpha():
                    new_player = Player(name=name, money=1500, in_jail=False)
                    session.add(new_player)
                    session.commit()
                    self.players.append(new_player)
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
                    console.print(f"[bold red]{player.name} is currently in jail. Skipping turn.[/bold red]")
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
                                        rolling = False
                                    session.commit()
                                    break
                                elif jail_choice == "n":
                                    console.print("[red]You chose not to pay. Going to jail.[/red]")
                                    player_obj.position = 10
                                    player_obj.in_jail = True
                                    rolling = False
                                    session.commit()
                                    break
                                else:
                                    console.print("[red]Invalid input. Please try again.[/red]")

                        session.commit()
                        console.print(f":arrow_right: [cyan]{player.name} is now at position {player_obj.position}[/cyan]")

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
