from utils import get_input

BASE = 5
DIGITS = ["=", "-", "0", "1", "2"]
OFFSET = 2


def snafu_to_decimal(snafu: str) -> int:
    return sum(
        [
            (DIGITS.index(s) - OFFSET) * (BASE**idx)
            for idx, s in enumerate(reversed(snafu))
        ]
    )


def decimal_to_snafu(decimal: int) -> str:
    snafu = ""

    while decimal > 0:
        remainder = decimal % BASE
        snafu += DIGITS[remainder - OFFSET - 1]
        carry = 1 if remainder >= 3 else 0
        decimal = decimal // BASE + carry

    return snafu[::-1]


def part1(data):
    print("Part1:", decimal_to_snafu(sum([snafu_to_decimal(t) for t in data])))


if __name__ == "__main__":
    data = get_input(day=25)
    part1(data)
