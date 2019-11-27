''' Implementing a decorator that quantifies and returns the execution time of any function '''

import timeit

def timeTaken(func):
    def inner():
        initial = timeit.default_timer()
        
        func()
        
        print("The time taken to execute the function is :",timeit.default_timer()-initial)
    return inner()

@timeTaken
def sumofsquarenum():
    j=0
    for i in range(0,10):
        j+=i*i
    print("sum of squares of 10 numbers: ",j)

        
        