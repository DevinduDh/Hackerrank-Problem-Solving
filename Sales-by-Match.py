# Sales by Match
n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

freq = {}
count = 0
for item in ar:
    if item in freq:
        freq[item] = freq[item] + 1
    else:
        freq[item] = 1

print(freq)
new_freq = {key: val for key, val in freq.items() if val != 1}
print(new_freq)

for key, val in new_freq.items():
    res = val // 2
    if res == 1:
        count = count + 1
    else:
        count = count + res

print(count)
