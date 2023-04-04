from utils import get_input


def part1(data):
    # A/X - Rock  ||  B/Y - Paper  ||  C/Z - Scisors
    shape_score = {"X": 1, "Y": 2, "Z": 3}
    rounds_score = {0: "BX, CY, AZ", 3: "AX, BY, CZ", 6: "AY, BZ, CX"}
    # Invert the previous dict
    round_score = {
        f"{r[0]} {r[1]}": score
        for (score, rounds) in rounds_score.items()
        for r in rounds.split(", ")
    }

    score = [shape_score[d[2]] + round_score[d] for d in data]
    print("Score:", sum(score))


def part2(data):
    # X - Lose  ||  Y - Draw  ||  Z - Win
    round_score = {"X": 0, "Y": 3, "Z": 6}
    # A - Rock  ||  B - Paper  ||  C - Scisors
    # Score of the shape on each round (1-Rock, 2-Paper, 3-Rock)
    shapes_score = {1: "BX, AY, CZ", 2: "CX, BY, AZ", 3: "AX, CY, BZ"}
    # Invert the previous dict
    shape_score = {
        f"{r[0]} {r[1]}": score
        for (score, rounds) in shapes_score.items()
        for r in rounds.split(", ")
    }

    score = [shape_score[d] + round_score[d[2]] for d in data]
    print("Score:", sum(score))


if __name__ == "__main__":
    data = get_input(day=2)
    part1(data)
    part2(data)
