nums = []
x = int(input())
while x != -1:
    nums.append(x)
    x = int(input())
big = nums[0]
for i in nums:
    if i > big:
        big = i
print(big)