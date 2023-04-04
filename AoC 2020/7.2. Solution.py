filepath = "7.1. Puzzle input.txt"
#filepath = "7.1. Puzzle example.txt"

with open(filepath) as fp:
    rules = fp.readlines()

# Remove whitespace characters like \n at the end of each line
rules = [x.strip() for x in rules]


def exploreBag(summary, inner, possible = set()):
    if inner in summary.keys():
        for bag in summary[inner]:
            possible.add(bag)
            possible = exploreBag(summary, bag, possible)
    return possible


def exploreContainerBag(summary, outer, subBags = 0):
    inner_bags = summary[outer]
    if (inner_bags):
        for bag in inner_bags.keys():
            mult = int(inner_bags[bag])
            subBags += mult*exploreContainerBag(summary, bag, 1)
    return subBags


inner_to_outer = {}
outer_to_inner = {}

for rule in rules:
    spacer = rule.index("contain")
    base = rule[:spacer-6]
    separated = rule[spacer+8:-1].split(", ")
    if (separated != ["no other bags"]):
        inner = [" ".join(i.split(" ")[1:-1]) for i in separated]
        outer = {" ".join(i.split(" ")[1:-1]):" ".join(i.split(" ")[0]) for i in separated}
    else:
        inner = []
        outer = {}
    
    outer_to_inner[base] = outer

    for bag in inner:
        if bag in inner_to_outer.keys():
            inner_to_outer[bag] = inner_to_outer[bag] + [base]
        else:
            inner_to_outer[bag] = [base]


# print(inner_to_outer)
number = len(exploreBag(inner_to_outer, "shiny gold"))
print(number)

# print(outer_to_inner)
number = exploreContainerBag(outer_to_inner, "shiny gold")
print(number)



    