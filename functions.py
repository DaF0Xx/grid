
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