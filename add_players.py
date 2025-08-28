from sqlalchemy.orm import sessionmaker
from engine import engine
from tables import Player

Session = sessionmaker(bind=engine)
session = Session()

# Add test players
player1 = Player(name="Alice", money=1500, position=0, in_jail=False)
player2 = Player(name="Bob", money=-100, position=5, in_jail=False)  # Bankrupt player
player3 = Player(name="Charlie", money=800, position=10, in_jail=True)

session.add_all([player1, player2, player3])
session.commit()
print("Added 3 test players to database")
session.close()