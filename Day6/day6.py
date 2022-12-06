with open("input.txt", "r") as f:
    # do stuff
    msg = f.read()


def get_index(string, length):
    for i in range(length-1, len(string)):
        if len(set(string[i - (length-1):i + 1])) == length:
            return i+1


# part 1
print(get_index(msg, 4))

# part 2
print(get_index(msg, 14))
