from .players import Initial  

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

# The input of names begins at the initial of the game
init = Initial()

game_state = {
    "start":init,
    "number": init._number,
    "players": init.players,   
    "ownership": {},
    "turn": 0,
    "dice": (0, 0),
}
