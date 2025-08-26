from players import Dice, Initial
initial= Initial()
# rules=Dice_rule()

import random
# ANSI colors
RESET = "\033[0m"
RED = "\033[91m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"

# 40 tiles for the board (simplified names)
TILES = [
    "GO", "Med", "CC", "Balt", "Inco", "RR", "Orie", "Chance", "Verm", "Conn",
    "Jail", "StC", "Elec", "Vir", "Comm", "StJ", "RR", "Ten", "Comm", "NY",
    "Free", "Kent", "CC", "IndAve", "IllAve", "RR", "AtlAve", "Vent", "Water", "PacAve",
    "Go2J", "RR", "NC", "CC", "Pen", "Short", "Chance", "Park", "Lux", "Board"
]

# Centralized Game State
game_state = {
    "players": [
        {"name": "P1", "pos": 0, "money": 1500, "owned": [], "color": RED},
        {"name": "P2", "pos": 0, "money": 1500, "owned": [], "color": BLUE}
    ],
    "ownership": {},   # tile index → owner name
    "turn": 0,         # index of whose turn it is (0 = P1, 1 = P2)
    "dice": (0, 0),    # last dice roll (d1, d2)
}


# ─── BOARD DRAWING ───────────────────────────────────────────

def format_tile(index):
    """Return a tile as a rectangular box (taller + wider)."""
    TILE_W = 16   # width
    TILE_H = 6    # height
    tile = TILES[index]

    # ownership / player markers
    marker = ""
    if index in game_state["ownership"]:
        marker += GREEN + f"[{game_state['ownership'][index]}*]" + RESET
    for p in game_state["players"]:
        if p["pos"] == index:
            marker += p["color"] + f"[{p['name']}]" + RESET

    # Build box
    top = "+" + "-" * (TILE_W - 2) + "+"
    bot = "+" + "-" * (TILE_W - 2) + "+"
    mid_lines = []
    mid_lines.append(f"|{index:02}:{tile}".ljust(TILE_W - 1) + "|")
    mid_lines.append(f"|{marker}".ljust(TILE_W - 1) + "|")
    # fill rest with empty lines for height
    while len(mid_lines) < TILE_H - 2:
        mid_lines.append("|" + " " * (TILE_W - 2) + "|")

    return [top] + mid_lines + [bot]


def draw_row(indices):
    """Draw a row of tiles side by side."""
    lines = ["" for _ in range(6)]  # 6 lines tall
    for idx in indices:
        tile_lines = format_tile(idx)
        for i in range(6):
            lines[i] += tile_lines[i]
    print("\n".join(lines))


def dice_tile():
    """Returns an ASCII-art tile with two dice side by side."""
    return [
        "+--------------+",
        "| ⚀      ⚂    |",
        "|              |",
        "|   ⚄     ⚁   |",
        "|              |",
        "+--------------+",
    ]


def draw_board():
    TILE_W = 16
    TILE_H = 6

    # --- Bottom row (Go to Jail) ---
    bottom_indices = list(range(0, 11))
    bottom_indices.reverse()
    bottom_row = [format_tile(i) for i in bottom_indices]

    # --- Left column (11 to 20) ---
    left_indices = list(range(11, 21))
    left_col = [format_tile(i) for i in left_indices]

    # --- Top row (21 to 30) ---
    top_indices = list(range(21, 31))
    top_row = [format_tile(i) for i in top_indices]

    # --- Dice Tile (after 30th) ---
    dice = dice_tile()

    # --- Right column (31 to 39) ---
    right_indices = list(range(31, 40))
    right_col = [format_tile(i) for i in right_indices]

    # --- Print Top Row (with Dice at end) ---
    for line_idx in range(TILE_H):
        print("".join(tile[line_idx] for tile in top_row) + dice[line_idx])

    # --- Print Middle Rows (Left + spaces + Right) ---
    for l, r in zip(reversed(left_col), right_col):
        for line_idx in range(TILE_H):
            print(l[line_idx] + " " * (TILE_W * 9) + r[line_idx])

    # --- Print Bottom Row ---
    for line_idx in range(TILE_H):
        print("".join(tile[line_idx] for tile in bottom_row))


# ─── GAMEPLAY ────────────────────────────────────────────────

def take_turn():
    """Interactive turn for the current player."""
    players = game_state["players"]
    ownership = game_state["ownership"]

    # Current player and opponent
    player = players[game_state["turn"]]
    other = players[(game_state["turn"] + 1) % 2]

    print(f"\n--- {player['color']}{player['name']}{RESET}'s turn ---")

    # input(f"{player['name']} press Enter to roll dice... ")
    # d1, d2 = random.randint(1, 6), random.randint(1, 6)
    # roll = d1 + d2
    # game_state["dice"] = (d1, d2)
    # print(f"{player['name']} rolled {d1} + {d2} = {roll}")
    initial.choice()
    dice= Dice()

    # Move player
    player["pos"] = (player["pos"] + dice._roll) % 40
    tile_index = player["pos"]
    tile = TILES[tile_index]

    # Property logic
    if tile not in ["GO", "Jail", "Free", "Go2J", "Chance", "CC", "Comm"]:
        if tile_index not in ownership:
            print(f"{tile} (tile {tile_index}) is unowned.")
            choice = input(f"Do you want to buy {tile} for $100? (y/n): ").strip().lower()
            if choice == "y" and player["money"] >= 100:
                ownership[tile_index] = player["name"]
                player["owned"].append(tile_index)
                player["money"] -= 100
                print(f"{player['name']} bought {tile} for $100")
            else:
                print(f"{player['name']} chose not to buy {tile}")
        elif ownership[tile_index] != player["name"]:
            rent = 50
            player["money"] -= rent
            other["money"] += rent
            print(f"{player['name']} landed on {tile} owned by {ownership[tile_index]}")
            print(f"{player['name']} pays ${rent} rent")
        else:
            print(f"{player['name']} landed on their own property {tile}")
    else:
        print(f"{player['name']} landed on {tile}")

    # Balances
    print(f"{player['name']} balance: ${player['money']}")
    print(f"{other['name']} balance: ${other['money']}")

    # Draw board
    draw_board()

    # Switch turn
    game_state["turn"] = (game_state["turn"] + 1) % 2


# ─── DEMO ───────────────────────────────────────────────────

while True:
    take_turn()
