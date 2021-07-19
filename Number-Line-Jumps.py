x1 = 0
v1 = 3
x2 = 4
v2 = 2
# For the two kangaroos to be at the same place (x1+nv1) = (x2 + nv2) mathematically
# if we isolate n here we get the fraction n = (x2-x1)/(v1-v2)
# From the given constraints we know that x2>x1
# Now we have to ensure the condition that n is an integer because it is number of jumps
# hence if v1 != v2 and (x2 - x1) % (v1 - v2) == 0:
if (x2 > x1) and (v2 > v1):
    print("NO")
    exit()
else:
    if v1 != v2 and (x2 - x1) % (v1 - v2) == 0:
        print("YES")
        exit()
    else:
        print("NO")
        exit()
