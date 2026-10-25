from functions import build_matrix
from functions import render

height = 3 # Height of the grid
pos = [0,0] # Initial position

matrix = build_matrix(height)

storage = dict()
for coord in matrix:
    if pos != coord:
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