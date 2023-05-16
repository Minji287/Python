# 구구단을 입력받아 입력받은 단을 출력하는 프로그램을 작성하시오.

num = int(input("원하는 구구단을 입력하시오 : "))

print("   " + str(num) + "단")
for i in range(1, 10):
    print(str(num) + " * " + str(i) + " = " + str(num*i))
