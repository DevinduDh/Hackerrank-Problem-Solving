arr = [1,2,3,4,5,4,3,2,1,3,4]
count_1 = 0
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0

count_list = {"1": [], "2": [], "3": [], "4": [], "5": []}
max_count = []
for ele in arr:
    if ele == 1:
        count_1 = count_1 + 1
    elif ele == 2:
        count_2 = count_2 + 1
    elif ele == 3:
        count_3 = count_3 + 1
    elif ele == 4:
        count_4 = count_4 + 1
    else:
        count_5 = count_5 + 1

count_list['1'].append(count_1)
count_list['2'].append(count_2)
count_list['3'].append(count_3)
count_list['4'].append(count_4)
count_list['5'].append(count_5)

#print(count_list)

# Find item with Max Value in Dictionary
itemMaxValue = max(count_list.items(), key=lambda x: x[1])
#print('Maximum Value in Dictionary : ', itemMaxValue[1])
listOfKeys = list()
# Iterate over all the items in dictionary to find keys with max value
for key, value in count_list.items():
    if value == itemMaxValue[1]:
        listOfKeys.append(key)

for i in range(len(listOfKeys)):
    listOfKeys[i] = int(listOfKeys[i])
#print(min(listOfKeys))

if len(listOfKeys) == 1:
    print(listOfKeys[0])
else:
    print(min(listOfKeys))


