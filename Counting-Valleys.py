steps = 8
path = "UDDDUDUU"


current_level = 0
count = 0
for i in range(steps):
    if path[i] == 'U':
        current_level += 1
    elif path[i] == 'D':
        current_level -= 1
        if current_level == -1:
            count += 1
print(count)
