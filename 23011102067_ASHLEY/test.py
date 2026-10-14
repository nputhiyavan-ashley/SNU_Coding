import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, target = data[0], data[1]
    values = data[2 : 2 + n]

    earliest_index: dict[int, int] = {}
    for j, value in enumerate(values):
        complement = target - value
        if complement in earliest_index:
            print(earliest_index[complement], j)
            return
        if value not in earliest_index:
            earliest_index[value] = j

    print("NONE")


if __name__ == "__main__":
    main()