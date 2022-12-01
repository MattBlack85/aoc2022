def parse_file():
    food = []
    with open('day1.txt', 'r') as f:
        partial_sum = 0
        for line in f.readlines():
            if line == "\n":
                food.append(partial_sum)
                partial_sum = 0
                continue
            else:
                partial_sum += int(line.split("\n")[0])
    return food

def find_elf_with_more_calories():
    elf_food = parse_file()
    # Part1
    print(f"The elf that has carries most calories carries {max(elf_food)} calories")
    # Part 2
    elf_food.sort()
    elf_food.reverse()
    print(f"The 3 elves that carry more calories are carrying together {elf_food[0] + elf_food[1] + elf_food[2]} calories")


if __name__ == '__main__':
    find_elf_with_more_calories()
