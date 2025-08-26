from data import session
from tables import Player

def handle_chance_or_community(player_id):
    """
    Task 2: Chance/Community Chest
    - Just display a message, no effects implemented
    """

    player = session.query(Player).filter(Player.id == player_id).first()

    if player:
        print(f"{player.name} drew a Chance/Community Chest card. No effect applied.")
    else:
        print("Player not found!")


def check_bankruptcy(player_id):
    """
    Task 2: Bankruptcy
    - If money < 0, remove player from DB
    """

    player = session.query(Player).filter(Player.id == player_id).first()

    if player and player.money < 0:
        print(f"{player.name} is bankrupt and removed from the game!")
        session.delete(player)
        session.commit()
    elif player:
        print(f"{player.name} is still in the game with ${player.money}.")
    else:
        print("Player not found!")
