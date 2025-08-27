from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

def draw_chance_card(player_id):
    message = "You picked a Chance card. (No effect implemented.)"
    print(f"Player {player_id}: {message}")
    return message

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
            print(f"Player {player_id} is bankrupt and removed from the game.")
        else:
            print(f"Player {player_id} is safe with money: {money}")

# Test block
if __name__ == "__main__":
    draw_chance_card(player_id=1)
    check_bankruptcy(player_id=1)
    check_bankruptcy(player_id=3)
