# inputs: heights[list] , k = initial jump height
# 1 portion = 1 height increase

# height = [1,2,3,3,2]
# k = 1
# min number of portions to jump all hurdles
# max height - initial height
# 3 -1 = 2

n = 5
k = 4

height = [1, 6, 3, 5, 2]
if max(height) > k:
    print(max(height) - k)
else:
    print(0)