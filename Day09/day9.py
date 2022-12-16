import copy

with open("input.txt", "r") as f:
    # do stuff
    moves = [line.strip().split() for line in f.readlines()]


class Rope:
    def __init__(self, connected):
        s = [0, 0]
        self.head = [0, 0]
        self.tail = [0, 0]
        self.next: Rope = connected
        self.tail_visited = []

    def schedule_moves(self, direction, distance):
        for _ in range(int(distance)):
            self.move_head(direction)
            self.move_tail()

    def move_head(self, direction):
        if direction == "R":
            self.head[0] += 1
        elif direction == "L":
            self.head[0] -= 1
        elif direction == "U":
            self.head[1] += 1
        elif direction == "D":
            self.head[1] -= 1

    def move_tail(self):

        h_distance = self.head[0] - self.tail[0]
        v_distance = self.head[1] - self.tail[1]

        if abs(h_distance) + abs(v_distance) > 2:
            self.tail[0] += int(abs(h_distance) / h_distance)
            self.tail[1] += int(abs(v_distance) / v_distance)

        elif abs(h_distance) > 1:
            self.tail[0] += int(abs(h_distance) / h_distance)

        elif abs(v_distance) > 1:
            self.tail[1] += int(abs(v_distance) / v_distance)

        if self.tail not in self.tail_visited:
            self.tail_visited.append(copy.deepcopy(self.tail))

        self.update_next()

    def update_next(self):
        if self.next:
            self.next.head = self.tail
            self.next.move_tail()

    def print_state(self):
        print("Head: ", self.head, "Tail: ", self.tail)


head = Rope(Rope(Rope(Rope(Rope(Rope(Rope(Rope(Rope(Rope(None))))))))))
for move in moves:
    head.schedule_moves(*move)

print("Part 1 solution: ", len(head.tail_visited))
print("Part 2 solution: ", len(head.next.next.next.next.next.next.next.next.tail_visited))


