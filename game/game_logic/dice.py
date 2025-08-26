import random
from .game_state import game_state

def roll_dice():
    d1, d2 = random.randint(1, 6), random.randint(1, 6)
    game_state["dice"] = (d1, d2)
    return d1, d2
