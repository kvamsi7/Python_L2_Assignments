''' CAlCULATOR Program '''
import math

def factorial(x):
  
  if type(x) != int :
    return TypeError
  
  if(x == 0):
    return 1
  else:
    return x * factorial(x-1)

def log10(x):
  return math.log10(x)


def radian(degree=0):
  return round(degree*(math.pi/180),5)
