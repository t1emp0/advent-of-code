# filepath, step = "9.1. Example input.txt", 5
filepath, step = "9.1. Puzzle input.txt", 25

with open(filepath) as fp:
    nums = fp.readlines()

# Remove whitespace characters like \n at the end of each line
nums = [int(x.strip()) for x in nums]

for i in range(step, len(nums)-step):
    nums_subs = [nums[i]-x for x in nums[i-step: i]]
    if not any(x in nums[i-step: i] for x in nums_subs):
        invalid_num = nums[i]
        print(f"Invalid num: {invalid_num}")
        break

found = False
set_size = 1
while not found:
    set_size += 1
    new_set = [sum(nums[i:i+set_size]) for i in range(len(nums)-set_size+1) if all(invalid_num > x for x in nums[i:i+set_size])]
    found = invalid_num in new_set

set_index = new_set.index(invalid_num)
sumands = nums[set_index:set_index+set_size]
#print(f"Sumands: {sumands}")
print(max(sumands)+min(sumands))