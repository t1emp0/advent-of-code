# filepath = "3.1. Puzzle example.txt"
filepath = "3.1. Puzzle input.txt"

with open(filepath) as fp:
    lines = fp.readlines()

# you may also want to remove whitespace characters like \n at the end of each line
lines = [x.strip() for x in lines]

slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
map_length = len(lines[0])

mult = 1

for slope in slopes:
    current_x = 0
    current_y = 0
    trees = 0
    
    while current_y < len(lines):
        line = lines[current_y]
        if line[current_x] == "#":
            trees += 1
        current_x = (current_x + slope[1]) % map_length
        current_y += slope[0]
    print(f"Slope: {slope}, Total trees: {trees}")
    
    mult *= trees

print(mult)