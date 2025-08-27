from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

def add_go_money(player_id, amount=200):
    with engine.begin() as conn:
        conn.execute(
            text("UPDATE players SET money = money + :amount WHERE id = :id"),
            {"amount": amount, "id": player_id},
        )
        result = conn.execute(
            text("SELECT money FROM players WHERE id = :id"),
            {"id": player_id},
        )
        new_money = result.scalar()
        print(f"Player {player_id} passed GO → New money: {new_money}")

def send_to_jail(player_id):
    with engine.begin() as conn:
        conn.execute(
            text("UPDATE players SET position = 10, in_jail = TRUE, skip_turn = TRUE WHERE id = :id"),
            {"id": player_id},
        )
        print(f"Player {player_id} sent to Jail and will skip their next turn.")

# Test block (runs only if file is executed directly)
if __name__ == "__main__":
    add_go_money(player_id=1, amount=200)
    send_to_jail(player_id=2)
