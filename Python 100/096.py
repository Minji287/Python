d = [[0 for j in range(20)] for i in range(20)]

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(1, 20):
        if d[j][y] == 1:
            d[j][y] = 0
        else:
            d[j][y] = 1

        if d[x][j] == 1:
            d[x][j] = 0
        else:
            d[x][j] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()