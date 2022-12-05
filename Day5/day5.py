with open("input.txt", "r") as f:
    # do stuff
    state, moves = f.read().split("\n\n")

rows = state.split("\n")
moves = moves.strip().split("\n")
starting_columns = [[] for _ in rows]

for i, row in enumerate(rows[:-1]):
    for j, value in enumerate(row[1::4]):
        if value != " ":
            starting_columns[j].insert(0, value)

moves = [[int(c) for c in move.split() if c.isnumeric()] for move in moves]

# part 1
end_columns = starting_columns.copy()
for amount, start, end in moves:
    end_columns[end-1] += end_columns[start-1][-amount:]
    end_columns[start-1] = end_columns[start-1][:-amount]
print("".join([column[-1] for column in end_columns]))

# part 2
end_columns = starting_columns.copy()
for amount, start, end in moves:
    end_columns[end-1] += end_columns[start-1][:-amount-1:-1]
    end_columns[start-1] = end_columns[start-1][:-amount]
print("".join([column[-1] for column in end_columns]))