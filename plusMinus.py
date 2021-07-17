a = [4,3,-2,6,-4]
n = 5
positive = []
negative = []
zero = []
#positive ratio = 3/5
#negative ratio = 2/5

for i in range(n):
    if a[i] > 0:
        positive.append(a[i])
    elif a[i] < 0:
        negative.append(a[i])
    else:
        zero.append(a[i])

print("{0:.6f}".format(len(positive)/n))
'''
p_r = (len(positive))/n
n_r = (len(negative))/n
z_r = (len(zero))/n
print("positive ratio is {}".format(p_r))
print("negative ratio is {}".format(n_r))
print("zero ratio is {}".format(z_r))
'''