from functions import build_matrix
from functions import render

height = 3 # Height of the grid
matrix = build_matrix(height) # Our matrix of positions
char_pos = [0,0] # Initial character position
storage = dict() # Dictionary that will store each coord and its respective string

for coord in matrix:
    if char_pos != coord: # If the character's position isn't the same as coord, we assign a "." - if it is, "x"
        storage.update({tuple(coord):"."})
    else:
        storage.update({tuple(coord):"x"})

print(storage)
#print(matrix)
print(render(matrix))

running = True
while running:
    try:
        move = input("w, a, s, d: ").lower()
        if move == 'a':
            pos[0] -= 1
        elif move == 'd':
            pos[0] += 1
        elif move == 'w':
            pos[1] += 1
        elif move == 's':
            pos[1] -= 1
        else:
            print("Invalid move! try again.")
            continue
    except KeyboardInterrupt:
        print("\nExiting...")
        break

    print(f"position: {pos}")