def reverse(x,y,z):
    return z,y,x

ret = reverse(1,2,3)
print(ret) # 리턴값이 여러 개인 경우, 튜플 형식으로 리턴

r1, r2, r3 = reverse('a', 'b', 'c')
print(r1); print(r2); print(r3)