import random
from sqlalchemy.orm import sessionmaker
from engine import engine
from tables import Player
import time

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
                choice=input("DO YOU WANT TO CONTINUE? (y/n): ").strip().lower()
                if choice=="y":
                    print("Resuming existing game")
                    self.players=existing_players
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
                # strip is for removing spaces
                name = input(f"Enter player name {i+1}: ").strip()
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
                        print(f"{player.name} rolled: {dice.dice1} + {dice.dice2} = {dice.roll}")
                        player_obj = session.query(Player).filter_by(name=player.name).first()
                        if player_obj:
                            new_position = player_obj.position + dice.roll
                            player_obj.position = new_position % 40
                            session.commit()
                            print(f"{player.name} is now at position {player_obj.position}")
                        else:
                            print(f"Error: Could not find player {player.name} in the database.")
                        
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