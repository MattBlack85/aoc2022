def parse_file():
    items = []

    with open('day4.txt', 'r') as f:
        for line in f.readlines():
            l = line.split(",")
            items.append(
                    (l[0], l[1].replace("\n", ""))
                )

    return items


def main():
    sections = parse_file()

    # Part 1
    counter = 0
    
    for a, b in sections:
        start_a, end_a = a.split("-")
        start_b, end_b = b.split("-")
        set_a = set(range(int(start_a), int(end_a) + 1))
        set_b = set(range(int(start_b), int(end_b) + 1))

        if not set_b - set_a or not set_a - set_b:
            counter += 1

    print(f"The sections that fully itersect are {counter}")

    # Part 2
    counter = 0
    
    for a, b in sections:
        start_a, end_a = a.split("-")
        start_b, end_b = b.split("-")
        a_range = range(int(start_a), int(end_a) + 1)
        b_range = range(int(start_b), int(end_b) + 1)
        set_a = set(a_range)

        for el in b_range:
            set_a.add(el)

        if len(set_a) != len(a_range) + len(b_range):
            counter += 1

    print(f"The sections that itersect at all are {counter}")

if __name__ == "__main__":
    main()
