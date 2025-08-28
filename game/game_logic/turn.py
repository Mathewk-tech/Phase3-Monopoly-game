from .game_state import game_state, RESET
from .dice import roll_dice
from .movement import move_player
from .board import draw_board

def take_turn():
    players = game_state["players"]
    # Fixed code - get player by turn index from values:
    player = list(players.values())[game_state["turn"]]

    print(f"\n--- {player['name']}{RESET}'s turn ---")
    input(f"{player['name']} press Enter to roll dice... ")

    d1, d2 = roll_dice()
    roll = d1 + d2
    print(f"{player['name']} rolled {d1} + {d2} = {roll}")

    move_player(player, roll)

    # show balances
    for p in players.values():
        print(f"{p['name']} balance: ${p['money']}")

    # redraw board
    draw_board()

    # switch turn
    game_state["turn"] = (game_state["turn"] + 1) % len(players)
