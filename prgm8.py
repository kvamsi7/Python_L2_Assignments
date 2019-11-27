''' Implement a simple generator '''


def fibo():
    x,y = 0,1
    
    while True:
        yield x
        x,y = y,x+y
   
fib = fibo()
fib.__next__()


