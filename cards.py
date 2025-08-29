import random
from sqlalchemy.orm import sessionmaker
from engine import engine
from tables import ChanceCard, CommunityChestCard

Session = sessionmaker(bind=engine)
session = Session()

def draw_chance_card(player_name):
    cards = session.query(ChanceCard).all()
    
    if not cards:
        print("No Chance cards available.")
        return "No card drawn"

    selected_card = random.choice(cards)
    print(f"{player_name} drew a Chance card:")
    print(f"{selected_card.description}")
    return selected_card.description


def draw_community_chest_card(player_name):
    cards = session.query(CommunityChestCard).all()
    
    if not cards:
        print("No Community Chest cards available.")
        return "No card drawn"

    selected_card = random.choice(cards)
    print(f"{player_name} drew a Community Chest card:")
    print(f"{selected_card.description}")
    return selected_card.description
