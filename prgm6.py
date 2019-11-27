'''Use the super () function to inherit the parent methods '''

import math

class Sqroot:
    def sqrt(self,a):
        self.a = a
        return math.sqrt(self.a)

class Addition:
    def add(self,var1,var2):
        self.var1 = var1
        self.var2 = var2
        return(self.var1+self.var2)

class Subtraction:
    def sub(self,var1,var2):
        self.var1 = var1
        self.var2 = var2
        return(self.var1-self.var2)

class Multiplication:
    def mul(self,var1,var2):
        self.var1 = var1
        self.var2 = var2
        return(self.var1*self.var2)

class Division:
    def div(self,var1,var2):
        self.var1 = var1
        self.var2 = var2
        return(self.var1/self.var2)

class MathNew(Sqroot,Addition,Subtraction,Multiplication,Division):
    def __init__(self):
        super()

maths = MathNew()

print(maths.sqrt(5))
print(maths.add(10,20))
print(maths.sub(30,20))
print(maths.mul(5,4))
print(maths.div(20,5))