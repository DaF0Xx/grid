def move(key, coords, window):
    # w
    if key == 119:
        window.clear()
        coords[0] -= 1
        window.addstr(coords[0], coords[1], "X")

    # s
    elif key == 115:
        window.clear()
        coords[0] += 1
        window.addstr(coords[0], coords[1], "X")

    # a
    elif key == 97:
        window.clear()
        coords[1] -= 3
        window.addstr(coords[0], coords[1], "X")            

    # d
    elif key == 100:
        window.clear()
        coords[1] += 3
        window.addstr(coords[0], coords[1], "X")