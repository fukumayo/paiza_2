N, W, H = [int(i) for i in input().split(" ")]
list_1 = [None] * H 

for i in range(H):
    list_2 = [int(j) for j in input().split(" ")]
    list_1[i] = list_2

for i in range(1, W):
    list_1[0][i] += list_1[0][i-1]

for i in range(1, H):
    list_1[i][0] += list_1[i-1][0]

for i in range(1, H):
    for j in range(1, W):
        list_1[i][j] = list_1[i][j-1] + list_1[i-1][j] - list_1[i-1][j-1]

for i in range(N):
    y_1, x_1, y_2, x_2 = [int(j)-1 for j in input().split(" ")]
    if y_1 >= 1 and x_1 >= 1:
        sum = list_1[y_2][x_2] - list_1[y_1-1][x_2] - list_1[y_2][x_1-1] + list_1[y_1-1][x_1-1]
    elif y_1 == 0 and x_1 != 0:
        sum = list_1[y_2][x_2] - list_1[y_2][x_1-1]
    elif y_1 != 0 and x_1 == 0:
        sum = list_1[y_2][x_2] - list_1[y_1-1][x_2]
    else:
        sum = list_1[y_2][x_2]
    print(sum)
    