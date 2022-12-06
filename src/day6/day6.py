def parse_file():
    with open('day6.txt', 'r') as f:
        return f.read()


def main():
    stream = parse_file()

    start = 0
    end = 4
    while True:
        next_analysis = stream[start:end]

        if len(set(next_analysis)) == 4:
            break
        else:
            start += 1
            end += 1

    print(f"The answer is {end}")

    # Part 2
    start = 0
    end = 14
    while True:
        next_analysis = stream[start:end]

        if len(set(next_analysis)) == 14:
            break
        else:
            start += 1
            end += 1

    print(f"The answer is {end}")


if __name__ == "__main__":
    main()
