from .game_state import game_state, TILES, RESET, GREEN

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


def dice_tile():
    """Returns an ASCII-art tile with two dice side by side (ASCII safe)."""
    return [
        "+--------------+",
        "|   o      o   |",
        "|              |",
        "|   o      o   |",
        "|              |",
        "+--------------+",
    ]


def draw_board():
    TILE_W = 16
    TILE_H = 6

    # --- Bottom row (0–10 reversed) ---
    bottom_indices = list(range(0, 11))
    bottom_indices.reverse()
    bottom_row = [format_tile(i) for i in bottom_indices]

    # --- Left column (11–20) ---
    left_indices = list(range(11, 21))
    left_col = [format_tile(i) for i in left_indices]

    # --- Top row (21–30) ---
    top_indices = list(range(21, 31))
    top_row = [format_tile(i) for i in top_indices]

    # --- Dice Tile (after 30th) ---
    dice = dice_tile()

    # --- Right column (31–39) ---
    right_indices = list(range(31, 40))
    right_col = [format_tile(i) for i in right_indices]

    # --- Print Top Row (with Dice at end) ---
    for line_idx in range(TILE_H):
        print("".join(tile[line_idx] for tile in top_row) + dice[line_idx])

    # --- Print Middle Rows (Left + spaces + Right) ---
    middle_space = " " * (TILE_W * (len(top_row) - 1))
    for l, r in zip(reversed(left_col), right_col):
        for line_idx in range(TILE_H):
            print(l[line_idx] + middle_space + r[line_idx])

    # --- Print Bottom Row ---
    for line_idx in range(TILE_H):
        print("".join(tile[line_idx] for tile in bottom_row))
