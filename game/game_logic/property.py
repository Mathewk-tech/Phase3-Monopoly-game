from .game_state import game_state, TILES, RESET, GREEN

def handle_property(player, tile_index):
    ownership = game_state["ownership"]
    tile = TILES[tile_index]

    if tile in ["GO", "Jail", "Free", "Go2J", "Chance", "CC", "Comm"]:
        return  # special tiles, do nothing now

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
        owner = next(p for p in game_state["players"] if p["name"] == ownership[tile_index])
        player["money"] -= rent
        owner["money"] += rent
        print(f"{player['name']} pays ${rent} rent to {owner['name']}")
