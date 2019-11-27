''' Method Resolution Order '''

class First:    # class First
    def method1(self):
        print('First Class Method')

class Second(First):  #class Second inherits First
    def method1(self):
        print('Second Class Method')

class Third(First): # class Third inherits First
    def method1(self):
        print('Third Class Method')

class Fourth(Second,Third):     # class Fourth inherits both Second,Third
    def method1(self):
        print('Fourth Class Method')


fo = Fourth()
print(Fourth.mro())
(Fourth.__mro__)