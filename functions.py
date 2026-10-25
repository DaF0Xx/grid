
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
    storage = dict() # Dictionary that will store each coord and its respective string

    for coord in array:
        if pos != coord: # If the character's position isn't the same as coord, we assign a "." - if it is, "x"
            storage.update({tuple(coord):"."})
        else:
            storage.update({tuple(coord):"x"})

    grid = ""
    length, height = array[-1][0] + 1, array[-1][1] + 1 # [x, y], so the last coord (array[-1]) contains both the last x and last y. We add 1 because the coords start from [0, 0]
    
    for y in range(height):
        for x in range(length):
            grid += storage[(x, y)]
        grid += "\n"
    return grid