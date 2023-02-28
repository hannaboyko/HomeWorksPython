print("Welcome in calculator app!\n")

try:
    val_float1 = float(input("Please, type a first number: "))
except (ValueError, NameError):
    val_float1 = float(input("Please, type just a first number: "))
try:
    val_float2 = float(input("Please, type second number: "))
except (ValueError, NameError):
    val_float2 = float(input("Please, type just a second number: "))
try:
    val_operator = input("Please, choose operator:\n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/'\n Your answer: ")
except (ValueError, NameError):
    val_operator = float(input("Please, type just a number of operator: "))

if val_operator == '1':
    result = val_float1 + val_float2
elif val_operator == '2':
    result = val_float1 - val_float2
elif val_operator == '3':
    result = val_float1 * val_float2
elif val_operator == '4':
    result = val_float1 / val_float2

print(result)
