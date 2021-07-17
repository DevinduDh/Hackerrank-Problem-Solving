a = [[1,2,3],[4,5,6],[7,8,9]]
n=3
rightDiagSum = 0
leftDiagSum = 0

#right diagonal = a[0]a[0] + a[1][1] + a[2][2]
#left diagonal = a[2][0] + a[1][1] + a[0][2]
for i in range(n):
        rightDiagSum = rightDiagSum + a[i][i]
        leftDiagSum = leftDiagSum + a[i][n-1-i]
print(abs(rightDiagSum-leftDiagSum))
