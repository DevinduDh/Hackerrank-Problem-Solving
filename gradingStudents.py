grades_count = int(input("Number of grades:").strip())
grades = []

for i in range(grades_count):
    grades_item = int(input("Enter Grades:").strip())
    grades.append(grades_item)

print(grades)
result = 0
for x in grades:
    if x < 38:
        result = x
        print(x)
    elif (x + 1) % 5 == 0:
        result = x + 1
        print(result)
    elif (x + 2) % 5 == 0:
        result = x + 2
        print(result)
    else:
        result = x
        print(result)
