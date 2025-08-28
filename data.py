from sqlalchemy.orm import sessionmaker
from engine import engine
from tables import Player, Property, Game, ChanceCard, CommunityChestCard

Session = sessionmaker(bind=engine)
session = Session()

def add_player():
    name = input("Enter player name: ")
    position = int(input("Enter player's current position: "))
    new_player = Player(name=name, money=1500, position=position, in_jail=False)
    session.add(new_player)
    session.commit()
    print(f"Added player '{name}' successfully")

def add_property():
    name = input("Enter property name: ")
    price = int(input("Enter price: "))
    new_property = Property(name=name, price=price)
    session.add(new_property)
    session.commit()
    print(f"Added property '{name}' successfully")



def add_chancecard():
    description = input("Enter chance card description: ")
    new_chance = ChanceCard(description=description)
    session.add(new_chance)
    session.commit()
    print("Added chance card successfully")

def add_communitychestcard():
    description = input("Enter community chest card description: ")
    new_card = CommunityChestCard(description=description)
    session.add(new_card)
    session.commit()
    print("Added community chest card successfully")

if __name__ == "__main__":
    print("Hello! Who would you like to add?")
    print("1) Player")
    print("2) Property")
    print("3) Chance Card")
    print("4) Community Chest Card")
    
    choice = input("Enter one of the choices above: ")
    if choice == "1":
        add_player()
    elif choice == "2":
        add_property()
    elif choice == "3":
        add_chancecard()
    elif choice == "4":
        add_communitychestcard()
    else:
        print("Wrong input, please try again")
