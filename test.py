matrix = []

row = 3
col = 3

for i in range(row):
    for j in range(col):
        point = []
        point.append(i)
        point.append(j)
        matrix.append(point)

counter = 0
for i in matrix:
    if i[0] != counter:
        print()
        counter += 1
    print(i, end='')

print()