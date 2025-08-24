from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship,sessionmaker
from engine import engine
from tables import Player,Property,Game,Card,ChanceCard,CommunityChestCard


session=sessionmaker(bind=engine)
session=session()

def add_player():
    name=input("Enter player name: ")
    new_player=Player(name=name,money=1500)
    session.add(new_player)
    session.commit()
    print(f"Added {name} successfully")

    
def add_property():
    name=input("Enter player name: ")
    price=input("Enter price: ")
    new_property=property(name=name,price=price)
    session.add(new_property)
    session.commit()
    print(f"Added {name} successfully")

def add_card():
    name=input("Enter player name: ")
    new_card=Card(name=name)
    session.add(new_card)
    session.commit()
    print(f"Added {name} successfully")

def add_chancecard():
    name=input("Enter chance name: ")
    new_chance=ChanceCard(name=name)
    session.add(new_chance)
    session.commit()
    print(f"Added {name} successfully")

def add_communitychestcard():
    name=input("Enter player name: ")
    new_card=CommunityChestCard(name=name)
    session.add(new_card)
    session.commit()
    print(f"Added {name} successfully")


if __name__=="__main__":
    print("Hello!What would you like to add?")
    print("1)player")
    print("2)property")
    print("3)card")
    print("4)chance card")
    print("5)community chest card")
    
    choice=input("Enter one of the choices above: ")
    if choice=="1":
        add_player()
    elif choice=="2":
        add_property()
    elif choice=="3":
        add_card()
    elif choice=="4":
        add_chancecard()
    elif choice=="5":
        add_communitychestcard()
    else:
        print("Wrong input please try again")
    










