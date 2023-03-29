'''
Для завданнь 1-7 за основу можете взяти код із попередніх ДЗ.

1. Написати функцію яка приймає один параметр – список рядків my_list. Функція повертає новий список у якому міститься
елементи з my_list за таким правилом:
Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
Якщо на парному – залишити без зміни.
'''
import string
import random as rand

def my_reverse(list):
    result = list.copy()
    for k, v in enumerate(result):
        if (k + 1) % 2 != 0:
            result[k] = v[::-1]
    return result

result = my_reverse(['abc', 'def', 'woc', 'ouch'])
print(*result)

'''
2. Написати функцію яка приймає один параметр – список рядків my_list.
Функція повертає новий список у якому міститься елементи my_list у яких перший символ - буква "a".
'''
def my_reverse(list):
    result = []
    for v in list:
       if v.startswith('a'):
        result.append(v)
    return result

result = my_reverse(['abc', 'def', 'wow', 'auch'])
print(*result)

'''
3. Написати функцію яка приймає один параметр – список рядків my_list.
Функція повертає новий список у якому міститься елементи з my_list, у яких є символ - буква "a" на будь-якому місці.
'''
def a_list(list):
    result = []
    for v in list:
        if v.find('a') != -1:
         result.append(v)
    return result

result = a_list(['abc', 'deaf', 'waw', 'ouch'])
print(*result)

'''
4. Написати функцію яка приймає один параметр - список рядків my_list у якому може бути як рядки (type str) і цілі числа (type int).
Функція повертає новий список у якому містяться лише рядки з my_list.
'''
def row_list(list):
    result = []
    for s in list:
        if isinstance(s, str):
         result.append(s)
    return result

result = row_list([1, 2, 3, "11", "22", 33])
print(*result)

'''
5. Написати функцію яка приймає один параметр – рядок my_str.
Функція повертає новий список у якому містяться ті символи з my_str, які зустрічаються у рядку лише один раз.
'''
def one_time(str):
    result = ''
    my_len = len(str)
    for s in str:
        if my_len - len(str.replace(s, '')) == 1:
         result += s
    return result

result = one_time('122333455678900')
print(result)

'''
6. Написати функцію яка приймає один параметр - два рядки.
Функція повертає список у який помістити ті символи, які є в обох рядках хоча б один раз.
'''
def same_elements(str):
    result = []
    for element in str:
        if element in my_str_1:
          if element in my_str_2:
            result.append(element)
    return result

my_str_1 = 'abcdefg'
my_str_2 = 'abjjefzg'
result = same_elements(my_str_1 and my_str_2)
print(*result)

'''
7. Написати функцію яка приймає два параметри - два рядки.
Функція повертає список до якого входять ті символи, які є в обох рядках, але в кожному лише по одному разу.
'''
def same_element(str):
    result = []
    for element in str:
        if element in my_str_1:
            if len(my_str_1) - len(my_str_1.replace(element, '')) == 1:
                if len(my_str_2) - len(my_str_2.replace(element, '')) == 1:
                    result.append(element)
    return result

my_str_1 = 'aaaasdf1'
my_str_2 = 'asdfff2'
result = same_element(my_str_1 and my_str_2)
print(*result)

'''

8. Дано списки names та domains (створити самостійно). Написати функцію для генерування e-mail у форматі:
    "ім'я . число від 100 до 999 @ стрінга з літер довжиною від 5 до 7 символів . домен"
Прізвище та домен брати випадковим чином із заданих списків переданих у функцію у вигляді параметрів.
Рядок і число генерувати випадковим чином.
'''
names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]

rnd = rand.randrange(100, 999)
name = names[rand.randint(0, len(names) - 1)]
domain = domains[rand.randint(0, len(domains) - 1)]
s = ''.join(rand.choice(string.ascii_uppercase + string.digits) for _ in range(5))
result = f"{name}.{rnd}@{s}.{domain}"

print(result)
