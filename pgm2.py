# Exception Handling ---program 2 

try:
  val1 = int(input("Enter first Number: "))
  val2 = int(input("Enter second Number: "))
  #                                           ctrl + C for keybaord interrupt
  # print(val1/val2)                          if val2 = 0 Arithmetic Error
  # print(val1/val3)                          val3 is not defined as local or global namespace 

except KeyboardInterrupt:
  print(" Keyboard interrupt occured, ctrl + c is pressed")
except ArithmeticError:
  print(" Arithmetic Error raised")
except NameError:
  print(" NameError: val3 not defined")
else:
  print("No Errors found")
finally:
  print(" Ending the Progarm")

