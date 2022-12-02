with open("input.txt", "r") as f:
    # do stuff
    games = [line.split() for line in f.readlines()]


scoresheet_part_1 = {
    "X": 1, "Y": 2, "Z": 3, "A": {"X": 3, "Y": 6, "Z": 0}, "B": {"X": 0, "Y": 3, "Z": 6}, "C": {"X": 6, "Y": 0, "Z": 3}
}

scoresheet_part_2 = {
    "X": 0, "Y": 3, "Z": 6, "A": {"X": 3, "Y": 1, "Z": 2}, "B": {"X": 1, "Y": 2, "Z": 3}, "C": {"X": 2, "Y": 3, "Z": 1}
}

score = 0
for his, mine in games:
    score += scoresheet_part_2[mine] + scoresheet_part_2[his][mine]

print(score)
