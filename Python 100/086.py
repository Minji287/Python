n = int(input())
s = int()
i = 1

while True:
    s += i
    i += 1
    if s >= n:
        print(s)
        break