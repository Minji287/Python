class MyClass:
    def __init__(self, txt):
        self.var = txt
        print('MyClass 인스턴스 객체가 생성되었습니다')
    
obj = MyClass('철수!')
print(obj.var)