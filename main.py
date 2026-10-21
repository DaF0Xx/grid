height = 10
coords = (4, 7)
x, y = coords
isInLine = 0

for i in range(0, height):
    if i == y:
        isInLine = True
    for j in range(0, 2*height):
        if isInLine and j == x:
            print("X", end="")
            isInLine = False
        else:
            print(".", end="")
    print()