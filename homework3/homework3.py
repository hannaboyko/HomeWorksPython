# 1 homework звичайний варіант
new_value = 101
if new_value < 100:
    result = new_value / 2
else:
    result = new_value * -1
print(result)

# ternary operator
result = new_value / 2 if new_value < 100 else new_value * -1
print(result)

#########################################################
# 2 homework звичайний варіант
new_value = 50
if new_value < 100:
    result = 1
else:
    result = 0
print(result)

# ternary operator
result = 1 if new_value < 100 else 0
print(result)

#########################################################
# 3 homework звичайний варіант

new_value = 424
if new_value < 100:
    result = True
else:
    result = False
print(result)

# ternary operator
result = True if new_value < 100 else False
print(result)

#########################################################
# 4 homework

my_str = "qwer"
index = 5
if len(my_str) >= index:
    print(my_str)
else:
    print(my_str * 2)

#########################################################
# 5 homework

my_str = "qwer"
index = 5
if len(my_str) >= index:
    print(my_str)
else:
    print(my_str+my_str[::-1])
