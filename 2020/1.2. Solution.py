filepath = "1.1. Puzzle input.txt"

with open(filepath) as fp:
    nums = fp.readlines()

# you may also want to remove whitespace characters like \n at the end of each line
nums = [int(x) for x in nums]

nums_subs = [2020-x for x in nums]
interesection2 = [x for x in nums if x in nums_subs]
print(interesection2, interesection2[0]*interesection2[1])

nums_subs2 = [y-x for y in nums_subs for x in nums_subs]
interesection3 = [x for x in nums if x in nums_subs2 and x in nums_subs]
int3 = [x for x in nums_subs if x+534 in nums_subs]
print(interesection3)
print(int3)
