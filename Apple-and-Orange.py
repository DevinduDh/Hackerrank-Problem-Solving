s = 7
t = 11

a = 5
b = 15

m = 3
n = 2

apples = [-2, 2, 1]
oranges = [5, -6]
count_a = 0
count_b = 0
for i in range(m):
    if apples[i] <= 0:
        continue
    if ((a + apples[i]) >= s) and ((a + apples[i]) <= t):
        count_a = count_a + 1
print(count_a)

for j in range(n):
    if oranges[j] < 0 and ((b + oranges[j]) <= t) and ((b + oranges[j]) >= s):
        count_b = count_b + 1
print(count_b)
