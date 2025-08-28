import random

# Get players
players = []
players.append(input("Player 1 name: "))
players.append(input("Player 2 name: "))

# Take turns
current_player = 0

for turn in range(6):
    print("\n" + players[current_player] + "'s turn")
    input("Press Enter to roll...")
    roll = random.randint(1, 6)
    print("Rolled " + str(roll))
    
    # Next player's turn
    if current_player == 0:
        current_player = 1
    else:
        current_player = 0

print("Game Over!")