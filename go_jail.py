# Monopoly Game - GO and Jail

import psycopg2   # lets us talk to the database
import os         # lets us use environment variables
from dotenv import load_dotenv   # helps load our .env file

# loads the .env file so we can get our database link
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# used to connect to the database
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

def add_go_money(player_id, amount=200):
    # add money to a player when they pass GO
    cur.execute("UPDATE players SET money = money + %s WHERE id = %s", (amount, player_id))
    conn.commit()
    print("Player", player_id, "passed GO and got", amount)

def send_to_jail(player_id):
    # move a player to jail (position 10) and make them skip a turn
    cur.execute("UPDATE players SET position = 10, in_jail = TRUE WHERE id = %s", (player_id,))
    conn.commit()
    print("Player", player_id, "was sent to Jail")

# example runs
if __name__ == "__main__":
    add_go_money(1)   # player 1 gets money for passing GO
    send_to_jail(2)   # player 2 goes to jail

# close database connection
cur.close()
conn.close()
 