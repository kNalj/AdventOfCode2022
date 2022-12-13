with open("input.txt", "r") as f:
    # do stuff
    commands = []
    for command in f.readlines():
        commands += command.strip().split()

signals_str_sum = 0
register = 1
display = ""
for cycle, command in enumerate(commands, 1):
    if cycle in [20, 60, 100, 140, 180, 220]:
        signals_str_sum += cycle * register
    pixel_position = (cycle-1) % 40
    check = abs(pixel_position - register) < 2
    if check:
        display += "#"
    else:
        display += "."

    try:
        int(command)
    except ValueError:
        pass
    else:
        register += int(command)


print("Part 1 answer: ", signals_str_sum)
print()
for i, pixel in enumerate(display):
    print(pixel, end="")
    if not (i+1) % 40:
        print()