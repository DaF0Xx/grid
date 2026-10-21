
height = 10
coords = (4, 7)
x, y = coords

def pos(h):
    row = []
    for i in range(h):
        row.append(i)
    return row

def render(array):
    text = "."*array[-1]
    return text

print(render(pos(height)))