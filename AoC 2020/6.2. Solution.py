from functools import reduce

filepath = "6.1. Puzzle input.txt"

with open(filepath) as fp:
    forms = fp.readlines()

# Remove whitespace characters like \n at the end of each line
forms = [x.strip() for x in forms]

groups_set = []
group_set = set()

groups_list = []
group_list = []

for form in forms:
    if len(form) >= 1:
        for elem in form:
            group_set.add(elem)
        group_list.append(form)

    else:
        unified = [elem for elem in group_set if all(elem in g for g in group_list)]
        groups_list.append(unified)
        group_list = []

        groups_set.append(group_set)
        group_set = set()

size_anyone = reduce(lambda count, element: count + len(element), groups_set, 0)
size_all = reduce(lambda count, element: count + len(element), groups_list, 0)

print(f"Anyone said yes: {size_anyone}")
print(f"All said yes: {size_all}")
