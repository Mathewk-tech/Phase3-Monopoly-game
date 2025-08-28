from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

def draw_chance_card(player_id):
    print(f"Player {player_id}: You picked a Chance card.")

def draw_community_chest_card(player_id):
    print(f"Player {player_id}: You picked a Community Chest card.")

def check_bankruptcy(player_id):
    with engine.begin() as conn:
        result = conn.execute(
            text("SELECT money FROM players WHERE id = :id"),
            {"id": player_id},
        )
        money = result.scalar()
        if money is None:
            print(f"Player {player_id} does not exist.")
            return
        if money < 0:
            conn.execute(
                text("DELETE FROM players WHERE id = :id"),
                {"id": player_id},
            )
            print(f"Player {player_id} is bankrupt!")
        else:
            print(f"Player {player_id} has ${money}")

if __name__ == "__main__":
    draw_chance_card(1)
    draw_community_chest_card(1)
    check_bankruptcy(1)
    check_bankruptcy(3)
