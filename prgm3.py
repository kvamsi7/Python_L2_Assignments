''' handling exception'''

c = 0

def f2(x):
    
    try:
        c+= 1
        b = x + c
        print(c)
        return b
    except Exception as err:
        print(err)
print(f2(1))
print(c)   