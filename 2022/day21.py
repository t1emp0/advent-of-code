from utils import get_input
from sympy import solve, Symbol

equation = ""


def get_result(current, monkeys):
    if current.isnumeric():
        return current

    first, op, second = current.split(" ")
    first = get_result(monkeys[first], monkeys)
    second = get_result(monkeys[second], monkeys)

    return int(eval(f"{first} {op} {second}"))


def get_result2(current, monkeys):
    global equation

    if current.isnumeric():
        return current

    first, op, second = current.split(" ")

    if first == "humn":
        second = get_result2(monkeys[second], monkeys)
        equation = f"humn {op} {second}"
        return

    first = get_result2(monkeys[first], monkeys)
    second = get_result2(monkeys[second], monkeys)

    if not first:
        equation = f"({equation}) {op} {second}"
        return
    if not second:
        equation = f"{first} {op} ({equation})"
        return

    return int(eval(f"{first} {op} {second}"))


def part2(monkeys):
    monkeys["root"] = monkeys["root"].replace("+", "=")
    get_result2(monkeys["root"], monkeys)

    eq = equation.replace("=", "-")
    result = int(solve(eq, Symbol("humn"))[0])
    print(f"Part 2: {result:_}")


def part1(monkeys):
    result = get_result(monkeys["root"], monkeys)
    print(f"Part 1: {result:_}")


if __name__ == "__main__":
    data = get_input(day=21)
    monkeys = dict(d.split(": ") for d in data)
    part1(monkeys)
    part2(monkeys)
