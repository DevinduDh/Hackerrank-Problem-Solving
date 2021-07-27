x = 1
y = 2
z = 3

# checking if mouse is between cats
if x < z < y:
    if z - x == y - z:
        result = 'Mouse C'
    elif z - x > y - z:
        result = 'Cat B'
    elif z - x < y - z:
        result = 'Cat A'
elif x > z > y:
    if z - y == x - z:
        result = 'Mouse C'
    elif z - y < x - z:
        result = 'Cat B'
    elif z - y > x - z:
        result = 'Cat A'

# Now we have checked whether mouse is between the cats or not.If mouse is not between the cats,
elif z < x and z < y:
    if y - z == x - z:
        result = 'Mouse C'
    elif y - z < x - z:
        result = 'Cat B'
    elif y - z > x -z:
        result = 'Cat A'

elif z > x and z > y:
    if z - x == z - y:
        result = 'Mouse C'
    elif z - x > z - y:
        result = 'Cat B'
    elif z -x < z -y:
        result = 'Cat A'

print(result)