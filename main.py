
height = 2 # Height of the grid
matrix = [] # Variable that will contain the matrix of positions

for i in range(height): # We build our matrix using the height variable
    for j in range(2*height): # Here i put this instead of using a length variable to make the rendered grid look uniform (but i guess a length variable would be better)
        pos = []
        pos.append(i)
        pos.append(j)
        matrix.append(pos)

    
def render(array): # We declare a function that can render our matrix, so that it looks like a grid of dots in the terminal
    row = "."*(array[2][0] + 1)
    grid = (row + "\n") * (len(row)-1) + row
    return grid

print(matrix)
print(render(matrix))