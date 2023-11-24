nums = []

vstup = input()
vstup = vstup.split()

for i in vstup:
    i = int(i)
    if i != -1:
        nums.append(i)
    else:
        break

biggest = nums[0]
for i in nums:
    if i > biggest:
        biggest = i

nums.remove(biggest)

big = nums[0]

for i in nums:
    if i > big:
        big = i

print(big)