
height = 3 # Height of the grid
pos = [0,0] # Initial position

# We declare a function to build our matrix
def build_matrix(n):
    matrix = [] # Variable that will contain the matrix of positions
    for y in range(n):
        for x in range(2*n):
            point = []
            point.append(x)
            point.append(y)
            matrix.append(point)
    return matrix

# We declare a function that can render our matrix, so that it looks like a grid of dots in the terminal
def render(array, pos=None):
    row = "."*(array[-1][0] + 1) # array[-1][]0 is the last "x" in the coordinate
    grid = (row + "\n") * (array[-1][1]) + row # array[-1][1] is the last "y" in the coordinate
    return grid

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