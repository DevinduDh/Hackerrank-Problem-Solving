ar = []
n = 5
for i in range(n):
    num = int(input())
    ar.append(num)

ar.sort()
print(ar)
print(len(ar))
k = 22
new_ar = []
temp_ar = []
count = 0

for i in range(len(ar)):
    for j in range(i + 1, len(ar)):
        print("i = {}, j = {}".format(i,j))
        new_ar.append(ar[i])
        new_ar.append(ar[j])
        print(new_ar)
        if (new_ar[0] < new_ar[1]) and ((new_ar[0] + new_ar[1]) % k) == 0:
            count = count + 1
        new_ar = []


print(count)
