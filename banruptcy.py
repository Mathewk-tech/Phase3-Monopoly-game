from sqlalchemy.orm import sessionmaker
from engine import engine
from tables import Player

Session = sessionmaker(bind=engine)
session = Session()

def check_bankruptcy(player_obj):
   
    if player_obj.money < 0:
        print(f"{player_obj.name} is bankrupt and has been removed from the game.")
        session.delete(player_obj)
        session.commit()
        return True
    else:
        print(f"{player_obj.name} is safe with ${player_obj.money}.")
        return False


