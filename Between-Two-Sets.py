# Between two sets

a = [1]
b = [72, 48]

n = len(a)
m = len(b)

X = min(b)
Y = max(a)
X1 = []
X2 = []

for i in range(1, X + 1):
    # print("i = {}".format(i))
    for ele in b:
        # print("ele = {}".format(ele))
        if ele % i == 0:
            X1.append(i)

X1_final = [k for k in X1 if X1.count(k) == m]
test1 = list(set(X1_final))
print(test1)
for j in range(len(test1)):
    if test1[j] >= Y:
        for item in a:
            if test1[j] % item == 0:
                X2.append(test1[j])
X2_final = [p for p in X2 if X2.count(p) == n]

test = list(set(X2_final))
print(test)
print(len(test))
