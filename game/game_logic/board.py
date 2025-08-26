from .game_state import game_state, TILES, RESET, GREEN

TILE_W = 14
TILE_H = 5

def format_tile(index):
    """Return a tile as a rectangular box (balanced size)."""
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


def draw_board():
    # --- Bottom row (0–10 reversed) ---
    bottom_indices = list(range(0, 11))[::-1]
    bottom_row = [format_tile(i) for i in bottom_indices]

    # --- Left column (11–19) ---
    left_indices = list(range(11, 20))   # 9 tiles
    left_col = [format_tile(i) for i in left_indices]

    # --- Top row (20–30) ---
    top_indices = list(range(20, 31))    # 11 tiles
    top_row = [format_tile(i) for i in top_indices]

    # --- Right column (31–39) ---
    right_indices = list(range(31, 40))  # 9 tiles
    right_col = [format_tile(i) for i in right_indices]

    # --- Print Top Row (20–30) ---
    for line_idx in range(TILE_H):
        print("".join(tile[line_idx] for tile in top_row))

    # --- Print Middle Rows (align 30 & 31) ---
    middle_space = " " * (TILE_W * (len(top_row) - 2))
    max_rows = max(len(left_col), len(right_col))

    for i in range(max_rows):
        l_tile = left_col[::-1][i] if i < len(left_col) else [" " * TILE_W] * TILE_H
        r_tile = right_col[i] if i < len(right_col) else [" " * TILE_W] * TILE_H

        for line_idx in range(TILE_H):
            print(l_tile[line_idx] + middle_space + r_tile[line_idx])

    # --- Print Bottom Row (10–0) ---
    for line_idx in range(TILE_H):
        print("".join(tile[line_idx] for tile in bottom_row))

    print("\n=====================\n")



