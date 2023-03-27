####### 1. Дано рядок: a. виведіть третій символ цього рядка. #########

value = "Hallelujah"
print(value[2])

####### 1. Дано рядок: b. виведіть передостанній символ цього рядка. #########

value = "Hallelujah"
print(value[-2])

####### 1. Дано рядок: c. виведіть перші п'ять символів цього рядка. #########

value = "Hallelujah"
print(value[0:5])

####### 1. Дано рядок: d. виведіть весь рядок, крім двох останніх символів. #########

value = "Hallelujah"
print(value[0:-2])

####### 1. Дано рядок:  e. виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0, тому символи виводяться починаючи з першого). #########

value = "Hallelujah"
print(value[::2])

####### 1. Дано рядок:  f. виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка. #########

value = "Hallelujah"
print(value[1::2])

####### 1. Дано рядок: g. виведіть усі символи у зворотному порядку. #########

value = "Hallelujah"
print(value[::-1])

####### 1. Дано рядок: h. виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього. #########

value = "Hallelujah"
print(value[-1::-2])

####### 1. Дано рядок: i. виведіть довжину цього рядка. #########

value = "Hallelujah"
print(len(value))

#################### ЗАВДАННЯ 2 ####################

value = "Lorem ipsum dolor sit amet consectetur adipiscing elit"
result = value.count(" ") + 1
print("in this string we have:", result, "words")


#################### ЗАВДАННЯ 3 ####################
def find_all(a_str, sub):
    _result = []
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return _result
        _result.append(start)
        start += len(sub)  # use start += 1 to find overlapping matches


value4 = "Lorem ipsum dolor set amt con$ectetur adipiscing elit"
indexes = find_all(value4, "$")
print('exercise 3: ', ' '.join(map(str, indexes)))


#################### ЗАВДАННЯ 4 ####################
def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]

value6 = "Lorem ipsum dolor s$t amet consectetur adipiscing elit"
new_v = value6
for i in find_all(value6, 'i')[1:-1]:
    new_v = replacer(new_v, 'I', i)
print("exercise 4: ", new_v)
