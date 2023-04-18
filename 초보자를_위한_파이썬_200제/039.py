def add_number(n1, n2):
    ret = n1 + n2
    return ret

def add_txt(t1, t2):
    print(t1, t2)

ans = add_number(10, 15)
print(ans)
text1 = '대한민국~'
text2 = '만세!!' # 키워드 매개 변수
add_txt(text1, text2)

def func1(*args): # 가변 매개 변수
    print(args)

def func2(width, height, **kwargs):
    print(kwargs) # {'depth': 50, 'color': 'blue'}

func1()
func1(3,5,1,5)
func2(10,20, depth=50, color='blue')