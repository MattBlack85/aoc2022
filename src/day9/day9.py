def parse_file(test=False):
    if test is False:
        with open("day9.txt") as f:
            file_lines = f.readlines()

            lines = []
            for line in file_lines:
                split = line.strip("\n").split()
                lines.append((split[0], int(split[1])))
    else:
        # lines = [
        #     ("R", 4),
        #     ("U", 4),
        #     ("L", 3),
        #     ("D", 1),
        #     ("R", 4),
        #     ("D", 1),
        #     ("L", 5),
        #     ("R", 2),
        # ]

        lines = [
            ("R", 5),
            ("U", 8),
            ("L", 8),
            ("D", 3),
            ("R", 17),
            ("D", 10),
            ("L", 25),
            ("U", 20),
        ]

    return lines


def main():
    data = parse_file()

    tail = [(0, 0)]
    head = [(0, 0)]

    for direction, val in data:
        latest_tail = tail[-1]
        latest_head = head[-1]

        match (direction, val):
            case ("R", amount):
                for _ in range(1, amount + 1):
                    latest_head = (latest_head[0] + 1, latest_head[1])
                    head.append(latest_head)
                    if latest_head[0] - latest_tail[0] > 1:
                        # Move Head
                        latest_tail = (latest_head[0] - 1, latest_head[1])
                        tail.append(latest_tail)
            case ("U", amount):
                for _ in range(1, amount + 1):
                    latest_head = (latest_head[0], latest_head[1] + 1)
                    head.append(latest_head)
                    if latest_head[1] - latest_tail[1] > 1:
                        # Move Head
                        latest_tail = (latest_head[0], latest_head[1] - 1)
                        tail.append(latest_tail)
            case ("D", amount):
                for _ in range(1, amount + 1):
                    latest_head = (latest_head[0], latest_head[1] - 1)
                    head.append(latest_head)
                    if latest_tail[1] - latest_head[1] > 1:
                        # Move Head

                        latest_tail = (latest_head[0], latest_head[1] + 1)
                        tail.append(latest_tail)
            case ("L", amount):
                for _ in range(1, amount + 1):
                    latest_head = (latest_head[0] - 1, latest_head[1])
                    head.append(latest_head)
                    if latest_tail[0] - latest_head[0] > 1:
                        # Move Head
                        latest_tail = (latest_head[0] + 1, latest_head[1])
                        tail.append(latest_tail)

    print(f"Tail has been in {len(set(tail))} places")

    def update_snake():
        for index in range(1, 10):
            actual = snake[index]
            previous = snake[index - 1]

            if abs(previous[0] - actual[0]) > 1 or abs(previous[1] - actual[1]) > 1:
                # Are we moving down?
                if previous[1] < actual[1]:
                    if previous[0] == actual[0]:
                        # Move plain down
                        new_actual = (actual[0], actual[1] - 1)
                    else:
                        if previous[0] > actual[0]:
                            # Move diagonally down right
                            new_actual = (actual[0] + 1, actual[1] - 1)
                        else:
                            # Move diagonally down left
                            new_actual = (actual[0] - 1, actual[1] - 1)
                # Are we moving up?
                elif previous[1] > actual[1]:
                    if previous[0] == actual[0]:
                        # Move plain Up
                        new_actual = (actual[0], actual[1] + 1)
                    else:
                        if previous[0] > actual[0]:
                            # Move diagonally up right
                            new_actual = (actual[0] + 1, actual[1] + 1)
                        else:
                            # Move diagonally up left
                            new_actual = (actual[0] - 1, actual[1] + 1)
                # Are we moving right?
                elif previous[0] > actual[0]:
                    if actual[1] == actual[1]:
                        # Move plain right
                        new_actual = (actual[0] + 1, actual[1])
                    else:
                        if previous[1] > previous[0]:
                            # Move diagonally up right
                            new_actual = (actual[0] + 1, actual[1] + 1)
                        else:
                            # Move diagonally up left
                            new_actual = (actual[0] - 1, actual[1] + 1)
                # Are we moving left?
                elif previous[0] < actual[0]:
                    if actual[1] == actual[1]:
                        # Move plain left
                        new_actual = (actual[0] - 1, actual[1])
                    else:
                        if previous[1] > previous[0]:
                            # Move diagonally up right
                            new_actual = (actual[0] + 1, actual[1] + 1)
                        else:
                            # Move diagonally up left
                            new_actual = (actual[0] - 1, actual[1] + 1)

                snake[index] = new_actual
                tail_tracking.add(snake[-1])

    # Part 2
    snake = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    tail_tracking = set([(0, 0)])
    data = parse_file()

    for direction, val in data:
        head = snake[0]
        print(f"snake is: {snake}")

        match (direction, val):
            case ("R", amount):
                for _ in range(1, amount + 1):
                    head = (head[0] + 1, head[1])
                    snake[0] = head
                    update_snake()

            case ("L", amount):
                for _ in range(1, amount + 1):
                    head = (head[0] - 1, head[1])
                    snake[0] = head
                    update_snake()

            case ("U", amount):
                for _ in range(1, amount + 1):
                    head = (head[0], head[1] + 1)
                    snake[0] = head
                    update_snake()

            case ("D", amount):
                for _ in range(1, amount + 1):
                    head = (head[0], head[1] - 1)
                    snake[0] = head
                    update_snake()

    print(f"Tail has been in {len(tail_tracking)} places")


if __name__ == "__main__":
    main()
