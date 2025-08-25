# The number of players has to be input as a limit
# players to input their names ch the limit
# use count to check the number of players names meet the targeted number
# ask the player if they want to roll the dice 
# the player with the highest sum from the roll becomes player1

class Players():
        def __init__(self):            
            print("How many players will be playing")
            # sets a limit in the number of player
            self.number_input= input()
            # checks if the input is a number then converts to integer
            if self.number_input.isdigit():
                self._number=int(self.number_input)
                # seting minimum players to  be 2
                if self._number <2:
                    print("the minimum players are '2'")
                    return
                
            else:
                print("must be a number")
                return
            count= 0

            # makes sure the number of names match the set limit
            while count < self._number:
                name = input("Name of player ")
                # the player has only two attempts to give the correct form of name
                while not name.isalpha():
                    print ("name must be of only letters")
                    name = input("Name of player ")

                    # only letters allowed (no digits, no spaces)
                    if name.isalpha():  
                        print (name)
                    return
                
                count +=1            
                print("Do you want to roll the dice? y/n ")
                # rolling time
                choice= input()
                # making sure the player must role the dice to proceed
                while choice == "n":
                    print("You must roll the dice ")
                    print("Do you want to roll the dice? y/n ")
                # rolling time
                    choice= input()
                if choice == "y":
                    print("wel")
                else:
                    print("Its yes or no")
                    return
# ineriting the players class
class Dice(Players):
    def __init__(self):
        super().__init__()

Dice()