y = 1917

if y > 1918:
    if y % 400 == 0 or ((y % 4 == 0) and (y % 100 != 0)):
        result = '12.09.' + str(y)
        print(result)
    else:
        result = '13.09.' + str(y)
        print(result)

elif y <= 1917:
    if y % 4 == 0:
        result = '12.09.' + str(y)
        print(result)
    else:
        result = '13.09.' + str(y)
        print(result)

elif y == 1918:
    result = '26.09.' + str(y)
    print(result)
