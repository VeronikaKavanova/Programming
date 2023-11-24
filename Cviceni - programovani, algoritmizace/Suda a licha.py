nums = []
end = False

while end != True:
    vstup = input()
    vstup = vstup.split()
    for i in vstup:
        i = int(i)
        if i != -1:
            nums.append(i)
        else:
            end = True
            break

suda = []
licha = []
for i in nums:
    if i%2 == 0:
        suda.append(i)
    else:
        licha.append(i)

for i in suda:
    print(i,end = " ")

for i in licha:
    print(i,end = " ")
