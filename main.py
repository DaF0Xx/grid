
height = 5 # Height of the grid
matrix = [] # Variable that will contain the matrix of positions

# We build our matrix using the height variable
for y in range(height):
    for x in range(2*height): # Here i put this instead of using a length variable to make the rendered grid look uniform (but i guess a length variable would be better)
        point = []
        point.append(x)
        point.append(y)
        matrix.append(point)
    
# We declare a function that can render our matrix, so that it looks like a grid of dots in the terminal
def render(array, pos=None):
    row = "."*(array[-1][0] + 1) # array[-1][0] is the last "x" in the coordinate
    grid = (row + "\n") * (array[-1][1]) + row # array[-1][1] is the last "y" in the coordinate
    return grid

print(render(matrix))