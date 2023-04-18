class Add:
    def add(self, n1, n2):
        return n1+n2
    
class Mul:
    def mul(self, n1, n2):
        return n1*n2
    
class Calculator(Add, Mul): #Add, Mul class 상속
    def sub(self, n1, n2):
        return n1-n2
    
obj = Calculator()
print(obj.add(1, 2))
print(obj.sub(1, 2))
print(obj.mul(1, 2))