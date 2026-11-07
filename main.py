from functions import build_matrix
from functions import render

height = 10 # Height of the grid
matrix = build_matrix(height) # Our matrix of positions
character = {"position":[0,0]} # Character attributes
clear = "\x1B[2J\x1B[H\x1B[3J"

running = True
# Game Loop
while running:
    print(render(matrix, character["position"])) # Print the rendered matrix
    print(f"position: {character["position"]}") # Print the character's position

    # Ask for input so the character can move
    try:
        move = input("w, a, s, d: ").lower()
        if move == 'a':
            character["position"][0] -= 1
        elif move == 'd':
            character["position"][0] += 1
        elif move == 'w':
            character["position"][1] -= 1
        elif move == 's':
            character["position"][1] += 1
        else:
            print("Invalid move! try again.")
    except KeyboardInterrupt:
        print("\nExiting...")
        break

    print(clear, end="", flush=True)