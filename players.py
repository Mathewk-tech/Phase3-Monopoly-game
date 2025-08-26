# The number of players has to be input as a limit
# players to input their names ch the limit
# use count to check the number of players names meet the targeted number
# ask the player if they want to roll the dice 
# the player with the highest sum from the roll becomes player1
import random
# ineriting the players class
class Dice():
    def __init__(self):
        self.dice1=random.randint(1,6)
        self.dice2=random.randint(1,6)
        self._roll= self.dice1 + self.dice2
        
class Initial(Dice):
        def __init__(self):
            super().__init__()  

            while True:
                # sets a limit in the number of player
                print("How many players will be playing")
                self.number_input= input()

                # checks if the input is a number then converts to integer
                if self.number_input.isdigit():
                    self._number=int(self.number_input)
                    # seting minimum players to  be 2
                    if self._number <2:
                        print("the minimum players are '2'")
                    else:
                        break                        
                    
                else:
                    print("must be a number")
                    return

            # makes sure the number of names match the set limit
            self.players = []
            for j in range  (self._number):
                self._name = input(f"Name of player {j+1}: ")
                # only letters allowed (no digits, no spaces)
                while not self._name.isalpha():
                    print ("name must be of only letters.No spaces")
                    self._name = input(f"Name of player {j+1}: ") 
                self.players.append({"name":self._name, "score":0})
                                      
                  
        def choice(self): 
            for player in self.players:                    
                print(f"{player['name']},do you want to roll the dice? y/n ")
                # rolling time
                self._choice= input()
                # making sure the player must role the dice to proceed
                while self._choice == "n":
                    print("You must roll the dice ")
                    print("Do you want to roll the dice? y/n ")
                # rolling time
                    self._choice= input()
                if self._choice == "y":
                    print("well")                
                    print(f"{player['name']} has rolled a ")
                    # calling the dice class for a new roll
                    self._dice= Dice()                    
                    player['score']=self._dice._roll
                    print(player['score'])
                    # print (self.players)
                   

                else:
                    print("Its yes or no")
                    return
d=Initial()
d.choice()
class Dice_rule(Dice):
    def __init__(self):
        super().__init__()
        if self.dice1== self.dice2:
             print("You have to roll again")
             d.choice()
Dice_rule()
class Loop:
    def loop(self):
        while True:
         # let them roll dice more than once
            d.choice()        
           
Loop().loop()
