
height = 10
coords = (0,0)
x, y = coords
positions = [
    [0,0], [1,0], [2,0],
    [0,1], [1,1], [2,1],
    [0,2], [1,2], [2,2],
    ]
    
def render(array):
    row = "."*(array[2][0] + 1)
    grid = (row + "\n") * (len(row)-1) + row
    return grid

print(positions)
print(render(positions))