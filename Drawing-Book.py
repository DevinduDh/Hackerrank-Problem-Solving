n = 100
p = 23
page_count = []
if p == 1 or p == n:
    result = 0
elif n % 2 == 0:
    if n - 1 == p or n - 2 == p or p == 2 or p == 3:
        result = 1
    else:
        page_count.append(p // 2)  # counting from front
        page_count.append((n - p) // 2)  # counting from rear
        result = min(page_count)
elif n % 2 != 0:
    if n - 1 == p:
        result = 0
    elif p == 2 or p == 3 or p == n - 2 or p == n - 3:
        result = 1
    else:
        page_count.append(p // 2)  # counting from front
        page_count.append((n - p) // 2)  # counting from rear
        result = min(page_count)

# print(result)
