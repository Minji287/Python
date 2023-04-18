n = int(input())

if n // 3 == 1:
    print("spring")
elif (n - 3) // 3 == 1:
    print("summer")
elif (n - 6) // 3 == 1:
    print("fall")
else:
    print("winter")