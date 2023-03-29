# 1. Дано ціле число (int). Визначити скільки нулів у цьому числі.
my_int = 10110
s = str(my_int)
print(len(s) - len(s.replace('0', '')))

# 2. Дано ціле число (int). Визначити скільки нулів наприкінці цього числа. Наприклад для числа 1002000 - три нулі
my_int = 1002000
s = str(my_int)
print(len(s) - len(s.rstrip('0')))

'''
3. Дано списки my_list_1 та my_list_2.
Створити список my_result, який спочатку помістити
елементи на парних місцях my_list_1, а потім всі елементи на парних місцях my_list_2.
'''
my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
my_list_2 = [9, 10, 11, 12, 13, 14]

my_result = []
for k, v in enumerate(my_list_1):
    if (k + 1) % 2 == 0:
        my_result.append(v)

for k, v in enumerate(my_list_2):
    if (k + 1) % 2 == 0:
        my_result.append(v)

print(*my_result)

'''
4. Наведено список my_list. СТВОРИТИ НОВИЙ список new_list у якого перший елемент з my_list
стоїть на останньому місці. Якщо my_list [1,2,3,4], то new_list[2,3,4,1]
'''
my_list = [1, 2, 3, 4]
new_list = my_list[1:]
new_list.append(my_list[0])
print(*new_list)

'''
5. Даний список my_list. У цьому списку перший елемент переставити на останнє місце.
[1,2,3,4] -> [2,3,4,1]. Перестворювати список не можна! (використовуйте метод pop)
'''
my_list = [1, 2, 3, 4]
first = my_list.pop(0)
my_list.append(first)
print(*my_list)

'''
6. Дано рядок у якому є числа (розділяються пробілами).
Наприклад "43 більше ніж 34, але менше ніж 56". Знайти суму ВСІХ ЧИСЕЛ (А НЕ ЦИФР) у цьому рядку.
Для цього прикладу відповідь - 133. (використовуйте split та перевірку isdigit)
'''
example = "43 більше ніж 34, але менше ніж 56"
result = 0
for s in example.replace(',', '').split(' '):
    if s.isdigit():
        result += int(s)
print(result)
assert result == 133

'''
7. Наведено список чисел. Визначте, скільки в цьому списку елементів,
які більше суми двох своїх сусідів (ліворуч і праворуч), і НАДРУКАЙТЕ КІЛЬКІСТЬ таких елементів.
Останні елементи списку ніколи не враховуються, оскільки у них недостатньо сусідів.
Для списку [2,4,1,5,3,9,0,7] відповіддю буде 3, тому що 4> 2+1, 5> 1+3, 9>3+0.
'''
my_list = [2, 4, 1, 5, 3, 9, 0, 7]
result = 0
for k, v in enumerate(my_list):
    if k == 0 or k + 1 == len(my_list):
        continue
    if v > (my_list[k - 1] + my_list[k + 1]):
        result += 1

assert result == 3

'''
8. Даний список my_list, в якому можуть бути як рядки (type str), так і цілі числа (type int).
Наприклад [1, 2, 3, "11", "22", 33]
Створити новий список у який помістити лише рядки з my_list.
'''
my_list = [1, 2, 3, "11", "22", 33]
result = []
for s in my_list:
    if isinstance(s, str):
        result.append(s)

print(*result)

'''
9. Дано рядок my_str. Створити список в який помістити символи з my_str,
які зустрічаються в рядку ТІЛЬКИ ОДИН разів.
'''
my_str = '122333455678900'
result = ''
my_len = len(my_str)

for s in my_str:
    if my_len - len(my_str.replace(s, '')) == 1:
        result += s

assert result == '146789'

'''
10. Дано два рядки. Створити список, у якому помістити ті символи,
які є в обох рядках хоча б один раз.
'''
my_str_1 = 'abcdefg'
my_str_2 = 'abjjefzg'

result = []
for element in my_str_1:
    if element in my_str_2:
        result.append(element)
assert result == ['a', 'b', 'e', 'f', 'g']

'''
11. Дано два рядки. Створити список, у якому помістити ті символи, які є в обох рядках,
але в кожній ТІЛЬКИ З одного разу.
Приклад: для рядків "aaaasdf1" та "asdfff2" відповідь ["s", "d"], т.к. ці символи є в кожному рядку по одному разу
'''
my_str_1 = 'aaaasdf1'
my_str_2 = 'asdfff2'
result = []
for element in my_str_1:
    if len(my_str_1) - len(my_str_1.replace(element, '')) == 1:
        if len(my_str_2) - len(my_str_2.replace(element, '')) == 1:
            result.append(element)

assert result == ["s", "d"]
