from game_logic.turn import take_turn
from game_logic.board import draw_board
from game_logic.game_state import game_state

if __name__ == "__main__":
    # Show initial board before the first turn
    print("\n=== Initial Game State ===")
    for p in game_state["players"]:
        print(f"{p['name']} balance: ${p['money']}")
    draw_board()

    # Start the game loop
    while True:
        take_turn()
