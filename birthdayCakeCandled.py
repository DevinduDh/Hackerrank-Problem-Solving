
a = [5,7,8,9,4,5,7,8,9,9,7,8,9,9]
n = len(a)
count = 0
a.sort()
print(a)
b = max(a)


for i in range(n):
    if a[i] == b:
        count = count + 1
print(count)




