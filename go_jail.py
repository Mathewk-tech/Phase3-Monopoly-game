from data import session
from tables import Player

def add_money_on_go(player_id, amount=200):
    """
    When a player passes GO, add money to their balance.
    Default amount is $200.
    """
    player = session.query(Player).filter_by(id=player_id).first()
    if player:
        player.money += amount
        session.commit()
        print(f"{player.name} passed GO and received ${amount}. New balance: ${player.money}")
    else:
        print("Player not found.")

def send_to_jail(player_id):
    """
    Sends a player to jail.
    Moves them to position 10, sets in_jail=True, and skips their next turn.
    """
    player = session.query(Player).filter_by(id=player_id).first()
    if player:
        player.position = 10
        player.in_jail = True
        player.skip_turn = True
        session.commit()
        print(f"{player.name} was sent to Jail. They will skip their next turn.")
    else:
        print("Player not found.")

# Example test code
if __name__ == "__main__":
    # Replace with a real player id from your database
    add_money_on_go(1)
    send_to_jail(1)
