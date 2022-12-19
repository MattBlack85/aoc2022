import copy


def parse_file(test=True):
    if test is False:
        name = "day11.txt"
    else:
        name = "day11_test.txt"

    with open(name) as f:
        lines = f.readlines()
        lines = [line.strip("\n") for line in lines]
        monkeys = []
        index = 0

        for line in lines:
            if "Monkey" in line:
                monkeys.append({})
            elif "Starting items" in line:
                items = line.strip("Starting items: ").split(",")
                monkeys[index]["items"] = [int(n) for n in items]
            elif "Operation" in line:
                op = line.strip("Operation: new = old ").split()
                if len(op) == 2:
                    op = (op[0], int(op[1]))
                else:
                    op = (op[0], "self")
                monkeys[index]["op"] = op
            elif "Test" in line:
                test = line.strip("Test: divisible by ")
                monkeys[index]["test"] = int(test)
            elif line == "":
                index += 1
            elif "true" in line:
                true = line.strip("If true: throw to monkey ")
                monkeys[index]["true"] = int(true)
            elif "false" in line:
                false = line.strip("If false: throw to monkey ")
                monkeys[index]["false"] = int(false)

    return monkeys


def check_stress(actual_level, operator, val, manage_stress=True, monkey_mod=None):
    if operator == "*":
        if isinstance(val, int):
            stress_level = actual_level * val
        else:
            stress_level = actual_level * actual_level
    elif operator == "+":
        stress_level = actual_level + val

    if manage_stress is True:
        return stress_level // 3
    else:
        return stress_level % monkey_mod


def check_inspection(monkeys, stress=True, rounds=20, monkey_mod=None):
    monkey_count = []

    for _ in range(len(monkeys)):
        monkey_count.append(0)

    for _ in range(rounds):
        for i, m in enumerate(monkeys):
            while m["items"]:
                item_stress_level = m["items"].pop(0)
                monkey_count[i] += 1

                if stress is True:
                    new_stress_level = check_stress(item_stress_level, m["op"][0], m["op"][1], manage_stress=stress)
                else:

                    new_stress_level = check_stress(
                        item_stress_level, m["op"][0], m["op"][1], manage_stress=stress, monkey_mod=monkey_mod)

                if new_stress_level % m["test"] == 0:
                    monkeys[m["true"]]["items"].append(new_stress_level)
                else:
                    monkeys[m["false"]]["items"].append(new_stress_level)

    monkey_count.sort(reverse=True)
    print(f"Monkeys: {monkey_count}")
    print(f"The total is: {monkey_count[0] * monkey_count[1]}")


def main():
    monkeys = parse_file(test=False)

    monkey_mod = 1

    for m in monkeys:
        monkey_mod *= m["test"]

    # Part 1
    check_inspection(copy.deepcopy(monkeys))

    # Part 2
    check_inspection(copy.deepcopy(monkeys), stress=False, rounds=10000, monkey_mod=monkey_mod)


if __name__ == "__main__":
    main()
