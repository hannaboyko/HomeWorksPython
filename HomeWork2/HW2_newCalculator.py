print("Welcome in calculator app!\n")

try:
    val_float1 = float(input("Please, type a first number: "))
except ValueError:
    print("Please try one more time and type only numbers")
    exit()
try:
    val_float2 = float(input("Please, type second number: "))
except ValueError:
    print("Please try one more time and type only numbers")
    exit()
try:
    val_operator = input("Please, choose operator:\n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/'\n Your answer: ")
except ValueError:
    print("Please, type just a number of operator: ")
    exit()
try:
     res =  val_float1 / val_float2
except ZeroDivisionError:
        print("Sorry")

if val_operator == '1':
  print(val_float1 + val_float2)
elif val_operator == '2':
  print(val_float1 - val_float2)
elif val_operator == '3':
   print(val_float1 * val_float2)
elif val_operator == '4':
     if val_float2 == 0:
         print("You can't divide by zero!")
     else:  print(val_float1/val_float2)
elif val_operator > "4":
         print("You must choose from 1 to 4")
