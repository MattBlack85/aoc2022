from collections import defaultdict
from functools import lru_cache

import sys

sys.setrecursionlimit(2000)


def parse_file():
    with open("day7.txt", "r") as f:
        return f.readlines()


def main():
    # index -1
    # sub_index -1
    test_instructions = [
        "$ cd /",  # index 0
        "$ ls",
        "dir a",  # i[0] = dir
        "14848514 b.txt",  # i[1] = dir
        "8504156 c.dat",  # i[2] = dir
        "dir d",  # i[3] = dir
        "$ cd a",  # index 1 (real 0)
        "$ ls",
        "dir e",  # index 1 append
        "29116 f",  # index 1 append
        "2557 g",  # index 1 append
        "62596 h.lst",  # index 1 append
        "$ cd e",  # index 1 subindex 0
        "$ ls",
        "584 i",  # index 1 subindex 0
        "$ cd ..",  # index 1 subindex -1
        "$ cd ..",  # index 0
        "$ cd d",  # index 1
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]
    instructions = parse_file()

    fs = defaultdict(list)
    path = ()

    while instructions:
        _, command, *args = instructions.pop(0).strip("\n").split()

        if command == 'ls':
            while instructions and not instructions[0].startswith('$'):
                size = instructions.pop(0).split()[0]
                if size != 'dir':
                    fs[path].append(int(size))
        else:
            if args[0] == '..':
                path = path[:-1]
            else:
                new_path = path + (args[0],)
                fs[path].append(new_path)
                path = new_path

    @lru_cache(maxsize=None)
    def directory_size(path):
        size = 0

        for subdir_or_size in fs[path]:
            if isinstance(subdir_or_size, int):
                size += subdir_or_size
            else:
                size += directory_size(subdir_or_size)

        return size
    used = directory_size(('/',))
    free = 70000000 - used
    need = 30000000 - free

    small_dir_total = 0
    min_size_to_free = used

    # for path in fs:
    #     sz = directory_size(path, fs)

    #     if sz <= 100000:
    #         small_dir_total += sz
    #     if sz >= need and sz < min_size_to_free:
    #         min_size_to_free = sz

    small_dir_total = sum(filter(lambda s: s <= 100000, map(directory_size, fs)))
    min_size_to_free = min(filter(lambda s: s >= need, map(directory_size, fs)))
    print(small_dir_total)
    print(min_size_to_free)


if __name__ == "__main__":
    main()
