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
