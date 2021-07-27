n = 4
k = 1

bill = [3, 10, 2, 9]

b = 12
total = 0

for i in range(n):
    total = total + bill[i]

# print(total_1)
total_per_person = total / 2
# print(total_per_person)

anna_pay_actual = total_per_person - bill[k] / 2
# print(anna_pay_actual)

if anna_pay_actual == b:
    print("Bon Appetit")
else:
    print(b - anna_pay_actual)
