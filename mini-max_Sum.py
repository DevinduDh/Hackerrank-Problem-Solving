a = [4,3,8,-9,12,40]
a.sort()
print(a)
b = a[1:]
c = a[:(len(a)-1)]
print("b is {} ".format(b))
print("c is {} ".format(c))

sum_max = 0
sum_min = 0
for i in range(len(b)):
    sum_max = sum_max + b[i]


for j in range(len(c)):
    sum_min = sum_min + c[j]

print("{} {}".format(sum_min, sum_max))

