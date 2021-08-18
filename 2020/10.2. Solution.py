filepath = "10.1. Puzzle input.txt"
#filepath = "10.1. Example input2.txt"
#filepath = "10.1. Example input.txt"

with open(filepath) as fp:
    nums = fp.readlines()

# Remove whitespace characters like \n at the end of each line
nums = [0] + [int(x.strip()) for x in nums]
device = max(nums)+3
nums = sorted(nums)

diff_1 = [nums[i] for i in range(len(nums)-1) if nums[i+1]-nums[i]==1]
diff_3 = [nums[i] for i in range(len(nums)-1) if nums[i+1]-nums[i]==3]
q1 = len(diff_1) * (len(diff_3) + 1)
print( q1 ) 

def exploreJolts(future, count=1):
    if len(future)>1:
        current = future[0]
        count = exploreJolts(future[1:], count)
        #print("case1", count, future)
        if len(future)>2 and (future[2]-current <= 3):
            #print("case2", count, future)
            count = exploreJolts(future[2:], count+1)
            if len(future)>3 and (future[3]-current <= 3):
                #print("case3", count, future)
                count = exploreJolts(future[3:], count+1)
    if count % 1000000== 0:
        print(count)
    return count

print(exploreJolts(nums))

"""print(diff_3)
non_essential2 = [nums[i+1] for i in range(len(nums)-2) if nums[i+2]-nums[i]<=3]
removed_2 = [i for i in nums if i not in non_essential2]
non_essential3 = [removed_2[i+1] for i in range(len(removed_2)-2) if removed_2[i+2]-removed_2[i]<=3]
non_essential = len(non_essential2) - len(non_essential3)
print(pow(2, non_essential))"""

