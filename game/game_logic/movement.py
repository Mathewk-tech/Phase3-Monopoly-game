from .game_state import game_state, TILES
from .property import handle_property

def move_player(player, roll):
    player["pos"] = (player["pos"] + roll) % 40
    tile_index = player["pos"]
    tile = TILES[tile_index]

    print(f"{player['name']} landed on {tile}")

    # handle buying / rent if applicable
    handle_property(player, tile_index)
