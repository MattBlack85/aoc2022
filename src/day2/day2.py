points_d = {
    "Y": 2,
    "X": 1,
    "Z": 3,
}


def parse_file():
    tournament = []

    with open('day2.txt', 'r') as f:
        for line in f.readlines():
            a, b = line.split(" ")
            tournament.append((a, b.replace("\n", "")))

    return tournament


def main():
    # A rock
    # B Paper
    # C scissors
    # X Rock
    # Y Paper
    # Z Scissors
    results = parse_file()

    # PART 1
    points = 0

    for x, y in results:
        if x == "A" and y == "Y":
            points = points + 6 + points_d[y]
        elif x == "B" and y == "Z":
            points = points + 6 + points_d[y]
        elif x == "C" and y == "X":
            points = points + 6 + points_d[y]
        elif x == "A" and y == "Z":
            points = points + 0 + points_d[y]
        elif x == "B" and y == "X":
            points = points + 0 + points_d[y]
        elif x == "C" and y == "Y":
            points = points + 0 + points_d[y]
        elif x == "A" and y == "X":
            points = points + 3 + points_d[y]
        elif x == "B" and y == "Y":
            points = points + 3 + points_d[y]
        elif x == "C" and y == "Z":
            points = points + 3 + points_d[y]

    print(f"You made {points} points at rock scissors paper")

    # PART 2
    points = 0

    # X Lose
    # Y Draw
    # Z Win

    # Scissors 3
    # Rock 1
    # Paper 2

    for x, y in results:
        if y == "Z" and x == "A":
            points = points + 6 + 2
        elif y == "Z" and x == "B":
            points = points + 6 + 3
        elif y == "Z" and x == "C":
            points = points + 6 + 1

        elif y == "Y" and x == "A":
            points = points + 3 + 1
        elif y == "Y" and x == "B":
            points = points + 3 + 2
        elif y == "Y" and x == "C":
            points = points + 3 + 3

        elif y == "X" and x == "A":
            points = points + 0 + 3
        elif y == "X" and x == "B":
            points = points + 0 + 1
        elif y == "X" and x == "C":
            points = points + 0 + 2

    print(f"You made {points} points at rock scissors paper with the secret guide")


if __name__ == "__main__":
    main()
