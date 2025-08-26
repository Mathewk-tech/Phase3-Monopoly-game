from data import session
from tables import Player

def draw_chance_card(player_id):
    """
    Displays a generic Chance card message.
    This is only a placeholder and does not apply real effects.
    """
    player = session.query(Player).filter_by(id=player_id).first()
    if player:
        print(f"{player.name} drew a Chance card! (Effect not implemented)")
    else:
        print("Player not found.")

def draw_community_chest_card(player_id):
    """
    Displays a generic Community Chest card message.
    This is only a placeholder and does not apply real effects.
    """
    player = session.query(Player).filter_by(id=player_id).first()
    if player:
        print(f"{player.name} drew a Community Chest card! (Effect not implemented)")
    else:
        print("Player not found.")

def check_bankruptcy(player_id):
    """
    Checks if a player's money is below 0.
    If yes, the player is removed from the game.
    """
    player = session.query(Player).filter_by(id=player_id).first()
    if player:
        if player.money < 0:
            session.delete(player)
            session.commit()
            print(f"{player.name} has gone bankrupt and is removed from the game.")
        else:
            print(f"{player.name} is safe. Current balance: ${player.money}")
    else:
        print("Player not found.")

# Example test code
if __name__ == "__main__":
    # Replace with a real player id from your database
    draw_chance_card(1)
    draw_community_chest_card(1)
    check_bankruptcy(1)
