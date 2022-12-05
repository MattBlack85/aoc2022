import copy

CRATES = {
    "1": ["Q", "W", "P", "S", "Z", "R", "H", "D"],
    "2": ["V", "B", "R", "W", "Q", "H", "F"],
    "3": ["C", "V", "S", "H"],
    "4": ["H", "F", "G"],
    "5": ["P", "G", "J", "B", "Z"],
    "6": ["Q", "T", "J", "H", "W", "F", "L"],
    "7": ["Z", "T", "W", "D", "L", "V", "J", "N"],
    "8": ["D", "T", "Z", "C", "J", "G", "H", "F"],
    "9": ["W", "P", "V", "M", "B", "H"],
}


def parse_file():
    items = []

    with open('day5.txt', 'r') as f:
        for line in f.readlines():
            l = line.split(" ")
            items.append([l[1], l[3], l[5].strip("\n")])

    return items

def main():
    # Part 1 
    moves = parse_file()
    crates = copy.deepcopy(CRATES)
    
    for how_many, from_c, to_c in moves:
        for _ in range(int(how_many)):
            crates[to_c].append(crates[from_c].pop())

    f_str = ""
    for c in crates.values():
        f_str += c[-1]

    print(f"The crates at the top are {f_str}")

    # Part 2
    moves = parse_file()
    crates = copy.deepcopy(CRATES)
    
    for how_many, from_c, to_c in moves:
        temp_crates = []
        for _ in range(int(how_many)):
            temp_crates.append(crates[from_c].pop())
        temp_crates.reverse()
        crates[to_c] = crates[to_c] + temp_crates

    f_str = ""
    for c in crates.values():
        f_str += c[-1]

    print(f"The crates at the top using the CrateMover 9001 are {f_str}")

if __name__ == "__main__":
    main()
