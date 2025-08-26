from data import session
from tables import Player

def handle_special_action(player_id, action_type):
    """
    Task 1: GO & Jail
    - GO: Add $200 to player's balance
    - GO_TO_JAIL: Move to jail, set in_jail=True, skip_turn=True
    """

    player = session.query(Player).filter(Player.id == player_id).first()

    if not player:
        print("Player not found!")
        return

    if action_type == "GO":
        player.money += 200
        print(f"{player.name} passed GO! Collect $200. Balance: ${player.money}")

    elif action_type == "GO_TO_JAIL":
        player.position = 10  # Jail space
        player.in_jail = True
        player.skip_turn = True
        print(f"{player.name} goes directly to Jail and will skip their next turn.")

    session.commit()
