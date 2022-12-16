with open("input.txt", "r") as f:
    s = [[int(n) for n in elf.split("\n")] for elf in f.read().rstrip().split("\n\n")]

# part 1
print(max([sum(g) for g in s]))

# part 2
print(sum(sorted([sum(g) for g in s])[-3:]))
