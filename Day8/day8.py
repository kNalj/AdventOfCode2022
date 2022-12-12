with open("input.txt", "r") as f:
    forest = [[int(i) for i in line.strip()] for line in f.readlines()]

total = 0
maxi = 0
for row, trees in enumerate(forest):
    for column, height in enumerate(trees):

        visible = False
        if not list(filter(lambda a: a >= height, trees[:column])):
            visible = True
        if not list(filter(lambda a: a >= height, trees[column+1:])):
            visible = True
        if not list(filter(lambda a: a >= height, [forest[i][column] for i in range(row)])):
            visible = True
        if not list(filter(lambda a: a >= height, [forest[i][column] for i in range(row+1, len(trees))])):
            visible = True
        if visible:
            total += 1

        l = next((i for i, v in enumerate(list(reversed(trees[:column]))) if v >= height), [len(list(reversed(trees[:column])))])
        l = l + 1 if type(l) == int else l[0]
        r = next((i for i, v in enumerate(trees[column+1:]) if v >= height), [len(trees[column+1:])])
        r = r + 1 if type(r) == int else r[0]
        u = next((i for i, v in enumerate(list(reversed([forest[i][column] for i in range(row)]))) if v >= height), [len(list(reversed([forest[i][column] for i in range(row)])))])
        u = u + 1 if type(u) == int else u[0]
        d = next((i for i, v in enumerate([forest[i][column] for i in range(row+1, len(trees))]) if v >= height), [len([forest[i][column] for i in range(row+1, len(trees))])])
        d = d + 1 if type(d) == int else d[0]

        if (l * r * u * d) > maxi:
            maxi = (l * r * u * d)


print("Part 1 solution: ", total)

print("Part 2 solution: ", maxi)
