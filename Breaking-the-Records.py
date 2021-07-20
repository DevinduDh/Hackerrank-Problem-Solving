# Breaking the records
n = 10
scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

max_record = scores[0]
print("initial max record = {}".format(max_record))
max_count = 0

min_record = scores[0]
print("initial min record = {}".format(min_record))
min_count = 0

del scores[0]
print("scores = {}".format(scores))

for i in range(n - 1):
    if scores[i] > max_record:
        # print("{} > {}".format(scores[i], max_record))
        max_record = scores[i]
        max_count = max_count + 1
    elif scores[i] < min_record:
        # print("{} < {}".format(scores[i], max_record))
        min_record = scores[i]
        min_count = min_count + 1

print("max record count = {}".format(max_count))
print("min record count = {}".format(min_count))
