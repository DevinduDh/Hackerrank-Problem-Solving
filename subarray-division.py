n = 5
s = [1, 2, 1, 3, 2]
d = 3  # date is integer sum
m = 2  # month is number of segments
count = 0
total = 0
new_list = []
final_list = []
for i in range(n + 1):
    for j in range(i):
        new_list.append(s[j:i])

for ele in new_list:
    if len(ele) == m:
        final_list.append(ele)
# print(final_list)

for item in final_list:
    # print("item = {}".format(item))
    total = 0
    for i in range(m):
        # print("i = {}".format(i))
        total = total + item[i]
    # print("total = {}".format(total))
    if total == d:
        count = count + 1
# print(count)
