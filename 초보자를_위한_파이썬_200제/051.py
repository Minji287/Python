class MyClass:
    def sayHello(self):
        print('안녕하세요')
    def sayBye(self, name):
        print('%s! 다음에보자!' %name)

obj = MyClass()
obj.sayHello()
obj.sayBye('철수')