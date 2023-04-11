f1 = 1.0
f2 = 3.14
f3 = 1.56e3 # 지수형
f4 = -0.7e-4 # 지수형

print(f1)
print(f2)
print(f3)
print(f4)
print(4//2) # 몫을 구하는 연산자 //
print(5%3) # 나머지 연산자 %

c1 = 1+7j
print(c1.real)
print(c1.imag)
c2 = complex(2,3)
print(c2)

a = 1
b = 2
ret = a + b
print('a와 b를 더한 값은 ', end='')
print(ret , end='')
print('입니다.')

bit1 = 0x61
bit2 = 0x62
print(hex(bit1 & bit2))
print(hex(bit1 | bit2))
print(hex(bit1 ^ bit2))
print(hex(bit1 >> 1))
print(hex(bit1 << 2))