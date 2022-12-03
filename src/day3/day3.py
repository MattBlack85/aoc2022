import string

def parse_file(split=True):
    items = []

    with open('day3.txt', 'r') as f:
        for line in f.readlines():
            if split is True:
                l = int(len(line) / 2)
                items.append(
                    (line[:l], line[l:].replace("\n", ""))
                )
            else:
                items.append(line.replace("\n", ""))

    return items

def calculate_priority_val(priorities):
    p_sum = 0
    for p in priorities:
        if p in string.ascii_lowercase:
            p_sum += ord(p) - 96
        else:
            p_sum += ord(p) - 38

    return p_sum

def main():
    items = parse_file()
    priorities = []
    
    for item in items:
        for x in item[0]:
            if x in item[1]:
                priorities.append(x)
                break

    assert len(priorities) == len(items)

    # Part 1
    print(f"The sum of priorites is {calculate_priority_val(priorities)}")

    # Part 2
    new_items = parse_file(split=False)
    new_p = []
    
    for i in range(0, len(new_items), 3):
        for el in new_items[i]:
            if el in new_items[i+1] and el in new_items[i+2]:
                new_p.append(el)
                break

    print(f"The sum of priorites in 3-groups is {calculate_priority_val(new_p)}")


if __name__ == "__main__":
    main()
