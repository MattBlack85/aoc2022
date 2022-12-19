def parse_file():
    with open("day8.txt", "r") as f:
        lines = f.readlines()

    return [
        l.strip("\n") for l in lines
    ]


def example():
    return [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390",
    ]


def main():
    trees = parse_file()
    # trees = example()

    tot_trees = (len(trees) * 2 - 4) + len(trees[0]) * 2

    # Part 1
    for row_index, row in enumerate(trees[1:-1]):

        for index in range(1, len(trees[0]) - 1):
            actual_val = int(row[index])

            # Check the top edge
            top_edge_visible = True
            for x in range(row_index + 1):
                prev_value = int(trees[x][index])
                if actual_val <= prev_value:
                    top_edge_visible = False
                    break

            # Check the left edge
            left_edge_visible = True
            for x in range(index):
                prev_value = int(row[x])
                if actual_val <= prev_value:
                    left_edge_visible = False
                    break

            # Check the right edge
            right_edge_visible = True
            for x in range(len(trees[0]) - 1, index, -1):
                prev_value = int(row[x])
                if actual_val <= prev_value:
                    right_edge_visible = False
                    break

            # Check the bottom edge
            bottom_edge_visible = True
            for x in range(len(trees) - 1, row_index + 1, -1):
                prev_value = int(trees[x][index])
                if actual_val <= prev_value:
                    bottom_edge_visible = False
                    break

            if any([bottom_edge_visible, left_edge_visible,
                    right_edge_visible, top_edge_visible]):
                tot_trees += 1

    print(f"{tot_trees} are visible")

    max_scenic = 0

    # Part 2
    for row_index, row in enumerate(trees[1:-1]):

        for index in range(1, len(trees[0]) - 1):
            actual_val = int(row[index])

            # Check the top edge
            top_scenic_count = 0
            for x in range(row_index + 1, 0, -1):
                next_value = int(trees[x - 1][index])
                if next_value >= actual_val:
                    top_scenic_count += 1
                    break
                else:
                    top_scenic_count += 1

            # Check the left edge
            left_scenic_count = 0
            for x in range(index, 0, -1):
                prev_value = int(row[x - 1])
                if prev_value >= actual_val:
                    left_scenic_count += 1
                    break
                else:
                    left_scenic_count += 1

            # Check the right edge
            right_scenic_count = 0
            for x in range(index, len(trees[0]) - 1):
                next_value = int(row[x + 1])
                if next_value >= actual_val:
                    right_scenic_count += 1
                    break
                else:
                    right_scenic_count += 1

            # Check the bottom edge
            bottom_scenic_count = 0
            for x in range(row_index + 1, len(trees) - 1):
                prev_value = int(trees[x + 1][index])
                if prev_value >= actual_val:
                    bottom_scenic_count += 1
                    break
                else:
                    bottom_scenic_count += 1

            scenic_count = bottom_scenic_count * top_scenic_count * left_scenic_count * right_scenic_count

            if scenic_count > max_scenic:
                max_scenic = scenic_count

    print(f"The max scenic point is: {max_scenic}")


if __name__ == "__main__":
    main()
