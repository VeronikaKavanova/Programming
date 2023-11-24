nums = []
while len(nums) != 2:
    x = input()
    y = x.split()
    for i in y:
        nums.append(int(i)) 

print(nums[0]+nums[1])