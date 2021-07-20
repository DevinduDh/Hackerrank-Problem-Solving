# Electronics Shop
b = 5
n = 1
m = 1

keyboards = [4]
drives = [5]

total = []
final_purchase = []

for i in range(n):
    for j in range(m):
        total.append(keyboards[i]+drives[j])

print(total)
for item in total:
    if item <= b:
        final_purchase.append(item)

if len(final_purchase) != 0:
    print(max(final_purchase))
else:
    print(-1)



