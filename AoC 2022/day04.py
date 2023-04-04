from utils import get_input


def part1_part2(data):
    fully = 0
    partially = 0
    for d in data:
        [f, s] = d.split(",")
        f1, f2 = map(int, f.split("-"))
        s1, s2 = map(int, s.split("-"))

        # Fully contained pairs
        if f1 <= s1 <= s2 <= f2:
            fully += 1
        elif s1 <= f1 <= f2 <= s2:
            fully += 1
        # Partially contained pairs
        elif s1 <= f1 <= s2 <= f2:
            partially += 1
        elif f1 <= s1 <= f2 <= s2:
            partially += 1

    print("Fully contained:", fully)
    print("Partially contained:", fully + partially)


if __name__ == "__main__":
    data = get_input(day=4)
    part1_part2(data)
