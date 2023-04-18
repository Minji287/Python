n = int(input())
sum = int(0)

for i in range(1, n+1):    
    sum += i
    if sum >= n:
        print(i)
        break