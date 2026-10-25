from functions import build_matrix
from functions import render

height = 10 # Height of the grid
matrix = build_matrix(height) # Our matrix of positions
character = {"position":[0,0]} # Character attributes

running = True
while running:
    print(render(matrix, character["position"]))
    print(f"position: {character["position"]}")

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
            continue
    except KeyboardInterrupt:
        print("\nExiting...")
        break
