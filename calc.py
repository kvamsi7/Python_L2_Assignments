''' CAlCULATOR Program '''
import math

def fact(x):
  
  if type(x) != int :
    return TypeError
  
  if(x == 0):
    return 1
  else:
    return x * fact(x-1)

def log10(x):
  return math.log10(x)


def radToDeg(degree=0):
  return round(degree*(math.pi/180),5)

def trig(n):
  n = float(n)
  print(math.sin(n))
  print(math.cos(n))
  print(math.tan(n))





