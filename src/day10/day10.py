def parse_file(test=True):
    if test is False:
        name = "day10.txt"
    else:
        name = "day10_test.txt"

    with open(name) as f:
        lines = f.readlines()
        lines = [line.strip("\n").split(" ") for line in lines]
        final = []
        for line in lines:
            if len(line) == 1:
                final.append((line[0],))
            else:
                final.append((line[0], int(line[1])))
    return final


def main():
    data = parse_file(test=False)
    x = 1
    cycle = 0
    next_strenght_check = 20
    strenght_readings = []

    def check_strenght(nc):
        if cycle == next_strenght_check:
            strenght_readings.append(x * nc)
            nc += 40

        return nc

    while data:
        instruction = data.pop(0)

        match instruction:
            case ("noop",):
                cycle += 1
                next_strenght_check = check_strenght(next_strenght_check)
            case ("addx", val):
                for _ in range(2):
                    cycle += 1
                    next_strenght_check = check_strenght(next_strenght_check)
                x += val

    print(f"Readings: {sum(strenght_readings)}")

    # Part 2
    sprite_coord = 1
    screen = [
        "",
        "",
        "",
        "",
        "",
        "",
    ]
    screen_index = 0
    cursor = -1

    def check_draw(sc, cursor, si):
        sprite_full = [sc - 1, sc, sc + 1]

        if cursor in sprite_full:
            screen[screen_index] += "#"
        else:
            screen[screen_index] += "."

        if cursor == 39:
            cursor = -1
            si += 1

        return cursor, si

    data = parse_file(test=False)

    while data:
        instruction = data.pop(0)

        match instruction:
            case ("noop",):
                cursor += 1
                cursor, screen_index = check_draw(sprite_coord, cursor, screen_index)
            case ("addx", val):
                for _ in range(2):
                    cursor += 1
                    cursor, screen_index = check_draw(sprite_coord, cursor, screen_index)
                sprite_coord += val

    for row in screen:
        print(f"{row}\n")


if __name__ == "__main__":
    main()
