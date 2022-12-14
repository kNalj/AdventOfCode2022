with open("input.txt", "r") as f:
    # do stuff
    raw_monkeys = [raw_monkey.split("\n") for raw_monkey in f.read().split("\n\n")]


class Monkey:
    def __init__(self, monkey_id, items, operation, test, monkey_if_true, monkey_if_false):
        self.id = monkey_id
        self.items = items
        self.operation = operation
        self.test = test
        self.monkey_if_true = monkey_if_true
        self.monkeyt_if_false = monkey_if_false
        self.checked = 0

    @classmethod
    def from_list(cls, monkey_list: list) -> "Monkey":

        monkey_id = monkey_list[0].strip(":").split(" ")[1]
        starting_items = [int(item) for item in monkey_list[1].split(": ")[1].split(", ")]
        operation = monkey_list[2].split(" = ")[1]
        test = int(monkey_list[3].split(": ")[1].split()[-1])
        m_true = monkey_list[4].split()[-1]
        m_false = monkey_list[5].split()[-1]

        return Monkey(monkey_id, starting_items, operation, test, m_true, m_false)

    def __repr__(self):
        return f"Monkey {self.id}:\n" \
               f"\tStarting items: {self.items}\n" \
               f"\tOperation: new = {self.operation}\n" \
               f"\tTest: divisible by {self.test}\n" \
               f"\t\tIf true: throw to monkey {self.monkey_if_true}\n" \
               f"\t\tIf false: throw to monkey {self.monkeyt_if_false}\n"

    def perform_operation(self, value):
        return eval(self.operation, {"old": value})

    def perform_test(self, value):
        return (value % int(self.test)) == 0


monkeys = []
for i, monkey in enumerate(raw_monkeys):
    monkeys.append(Monkey.from_list(monkey))

for round in range(20):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.checked += 1
            new = monkey.perform_operation(item) // 3
            if monkey.perform_test(new):
                monkeys[int(monkey.monkey_if_true)].items.append(new)
            else:
                monkeys[int(monkey.monkeyt_if_false)].items.append(new)
        monkey.items.clear()

monkeys.sort(key=lambda x: x.checked, reverse=True)
print(monkeys[0].checked * monkeys[1].checked)


monkeys = []
prod = 1
for i, monkey in enumerate(raw_monkeys):
    m = Monkey.from_list(monkey)
    monkeys.append(m)
    prod *= int(m.test)
for round in range(10000):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.checked += 1
            new = monkey.perform_operation(item) % prod
            if monkey.perform_test(new):
                monkeys[int(monkey.monkey_if_true)].items.append(new)
            else:
                monkeys[int(monkey.monkeyt_if_false)].items.append(new)
        monkey.items.clear()

monkeys.sort(key=lambda x: x.checked, reverse=True)
print(monkeys[0].checked * monkeys[1].checked)
