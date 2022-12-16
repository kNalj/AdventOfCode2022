with open("input.txt", "r") as f:
    # do stuff
    rucksacks = [line.strip() for line in f.readlines()]


def letter_value(letter):
    if letter.upper() == letter:
        return ord(letter) - 64 + 26
    return ord(letter) - 70 - 26


result_p1 = sum([
    letter_value(list(set(rucksack[:len(rucksack) // 2]).intersection(rucksack[len(rucksack) // 2:]))[0])
    for rucksack in rucksacks
])
print(result_p1)


result_p2 = sum([
    letter_value(list(set(rucksack).intersection(rucksacks[i-1]).intersection(rucksacks[i-2]))[0])
    for i, rucksack in enumerate(rucksacks) if not (i+1) % 3
])
print(result_p2)
