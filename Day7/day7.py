with open("input.txt", "r") as f:
    # do stuff
    commands = [line for line in f.readlines()]


class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.files = []
        self.dirs = {"..": parent}

    def get_size(self):
        return sum([file.size for file in self.files]) + sum(directory.get_size() for name, directory in self.dirs.items() if name != "..")

    def sum_with_limit(self, limit=100000):
        return (self.get_size() if self.get_size() < limit else 0) + sum(directory.sum_with_limit() for name, directory in self.dirs.items() if name != "..")

    def find_sizes(self, output):
        # if self.get_size() >
        output.append(self.get_size())
        for name, directory in self.dirs.items():
            if name != "..":
                directory.find_sizes(output)


class File:
    def __init__(self, name, size):
        self.size = size
        self.name = name


def parse_command(input_str):
    if input_str.startswith("$"):
        parsed = input_str.strip().split(" ")[1:]
    else:
        parsed = input_str.strip().split(" ")

    if len(parsed) > 1:
        command, param = parsed
    else:
        command = parsed[0]
        param = None

    return command, param


def interpret_command(command, param, current_dir=None):
    if command == "cd":
        if param != "/":
            current_dir = current_dir.dirs[param]
    elif command == "dir":
        current_dir.dirs[param] = Dir(param, current_dir)
    elif command.isnumeric():
        current_dir.files.append(File(param, int(command)))

    return current_dir


root = Dir("/")
current_dir = root
for command in commands:
    current_dir = interpret_command(*parse_command(command), current_dir)
print("Part 1 solution: ", root.sum_with_limit())


sizes = []
root.find_sizes(sizes)
candidates = list(filter(lambda size: size > 30000000 - (70000000 - root.get_size()), sizes))
candidates.sort()
file_to_delete = candidates[0]
print("Part 2 solution: ", file_to_delete)
