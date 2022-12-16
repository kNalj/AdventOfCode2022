with open("input.txt", "r") as f:
    schedule = [[[int(area_num) for area_num in task.split("-")] for task in line.strip().split(",")] for line in f.readlines()]


def check_subset(task):
    first = set(list(range(task[0][0], task[0][1]+1)))
    second = set(list(range(task[1][0], task[1][1]+1)))

    return (first.issubset(second) or first.issuperset(second)), first.intersection(second)


subsets = 0
overlaps = 0

for task in schedule:
    if result := check_subset(task):
        issubset, overlap = result
        subsets += 1 if issubset else 0
        overlaps += 1 if overlap else 0


print(subsets)
print(overlaps)
