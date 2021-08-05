from collections import Counter  # Import counter

# Given array
a = [1, 1, 2, 2, 4, 4, 23, 12, 9]

# Get the frequencies of the elements in the array
arr = Counter(a)
# print(arr)
maxnum = 0

for i in range(100):  # range is given
    # print("i = {}".format(i))
    # print(maxnum)
    maxnum = max(maxnum, arr[i] + arr[i + 1])

print(maxnum)
