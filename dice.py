import random
from sqlalchemy.orm import sessionmaker
from engine import engine
<<<<<<< HEAD
from tables import Player, Board
from cards import draw_chance_card, draw_community_chest_card
from property import handle_player_landing,buy_property

from rich import print
from rich.console import Console
from rich.prompt import Prompt

=======
from tables import Player
import time
>>>>>>> origin/MP-2-dice-rolling

Session = sessionmaker(bind=engine)
session = Session()

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
        existing_players=session.query(Player).all()
        while True:
            if existing_players:
<<<<<<< HEAD
                console.print("-----------------------------------------")
                console.print("[bold red]WELCOME TO MONOPOLY![/bold red]")
                console.print("-----------------------------------------")
                console.print("[bold magenta]An existing game was found.[/bold magenta]")
                choice = Prompt.ask("[bold cyan]Do you want to continue?[/] (y/n)").strip().lower()
                if choice == "y":
                    console.print("[green]Resuming existing game[/green]")
                    console.print(" ")
                    self.players = existing_players
=======
                choice=input("DO YOU WANT TO CONTINUE? (y/n): ").strip().lower()
                if choice=="y":
                    print("Resuming existing game")
                    self.players=existing_players
>>>>>>> origin/MP-2-dice-rolling
                    return
                elif choice=="n":
                    print("Starting a new game")
                    for player in existing_players:
                        session.delete(player)
                    session.commit()
                    return
                else:
                    print("Wrong input,please try again")
                    continue
            else:
                return
                


    def get_players(self):
        while True:
            number_input = input("How many players will be playing? ")
            if number_input.isdigit():
                number = int(number_input)
                if number < 2:
                    print("Minimum number of players is 2.")
                elif number >8:
                    print("Maximum number of players is 8.")
                else:
                    break
            else:
                print("Please enter a valid number.")

        for i in range(number):
            while True:
<<<<<<< HEAD
                name = Prompt.ask(f"[bold magenta]Enter player name {i+1}[/]").strip()
                console.print(" ")
=======
                # strip is for removing spaces
                name = input(f"Enter player name {i+1}: ").strip()
>>>>>>> origin/MP-2-dice-rolling
                if name.isalpha():
                    new_player = Player(name=name, money=1500, in_jail=False)
                    session.add(new_player)
                    session.commit()
                    self.players.append(new_player)
                    break
                else:
                    print("Name must contain only letters (no spaces, digits, or special characters).")

    def play(self):
        duration=6000
        Start=time.time()

        while True:
            Stop=time.time()-Start
            if Stop>=duration:
                print("Times up!Gameover")
                return
            for player in self.players:
                rolling=True
                while rolling:
                    Stop=time.time()-Start
                    if Stop>=duration:
                        print("Times up!Gameover")
                        return
                    choice = input(f"{player.name}, do you want to roll the dice? (y/n): ").lower()
                    if choice == "y":
                        dice = Dice()
<<<<<<< HEAD
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
                        ##this handles the buying of property and been removed out of the game if u cant pay rent
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

=======
                        print(f"{player.name} rolled: {dice.dice1} + {dice.dice2} = {dice.roll}")
                        player_obj = session.query(Player).filter_by(name=player.name).first()
                        if player_obj:
                            new_position = player_obj.position + dice.roll
                            player_obj.position = new_position % 40
                            session.commit()
                            print(f"{player.name} is now at position {player_obj.position}")
                        else:
                            print(f"Error: Could not find player {player.name} in the database.")
                        
>>>>>>> origin/MP-2-dice-rolling
                        if dice.is_double():
                            print("Invalid!You rolled a double! Roll again.")
                            continue
                        else:
                            rolling=False
                    
                    elif choice == "n":
                        print("You must roll to play.")
                    else:
                        print("Invalid choice. Enter 'y' or 'n'.")


if __name__ == "__main__":
    game = Game()
    game.play()