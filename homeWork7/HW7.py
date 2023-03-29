'''
1. Наведено список рядків my_list. Створити новий список до якого помістити елементи з my_list за таким правилом:
Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
Якщо на парному – залишити без зміни. Завдання зробити за допомогою enumerate або range.
'''

my_list = ['abc', 'def', 'wow', 'ouch']
result = my_list.copy()
for k, v in enumerate(result):
    if (k + 1) % 2 == 0:
        result[k] = v[::-1]

assert result == ['abc', 'def'[::-1], 'wow', 'ouch'[::-1]]

'''
2. Наведено список рядків my_list. Створити новий список до якого помістити елементи my_list
у яких перший символ - буква "a".
'''
my_list = ['abc', 'def', 'wow', 'auch']
result = []
for v in my_list:
    if v.startswith('a'):
        result.append(v)

assert result == ['abc', 'auch']

'''
3. Наведено список рядків my_list. Створити новий список до якого помістити
елементи з my_list, у яких є символ - буква "a" на будь-якому місці.
'''
my_list = ['abc', 'deaf', 'waw', 'ouch']
result = []
for v in my_list:
    if v.find('a') != -1:
        result.append(v)

assert result == ['abc', 'deaf', 'waw']

'''
4) Даний список словників людей у форматі [{"name": "John", "age": 15}, ..., {"name": "Jack", "age": 45}]
а) Створити список і помістити туди ім'я наймолодшої людини. Якщо вік збігається – помістити всі імена наймолодших.
б) Створити список та помістити туди найдовше ім'я. Якщо довжина імені збігається - помістити такі імена.
в) Порахувати середню вік усіх людей із початкового списку.
'''
my_list = [{"name": "John", "age": 15}, {"name": "Denys", "age": 40}, {"name": "Mary", "age": 13},
           {"name": "Ylya", "age": 13}, {"name": "Jack", "age": 45}, {"name": "Ann", "age": 25},
           {"name": "Lil", "age": 26}]

the_youngest_names = []

age = float('inf')
for v in my_list:
    if v.get('age') <= age:
        age = v.get('age')

for v in my_list:
    if v.get('age') == age:
        the_youngest_names.append(v.get('name'))

# a
assert the_youngest_names == ["Mary", "Ylya"]

# _result = sorted(my_list, key=lambda i: i['age'])
# print(*_result)

the_most_longest_name = 0
result = []
for v in my_list:
    if len(v.get('name')) > the_most_longest_name:
        the_most_longest_name = len(v.get('name'))

for v in my_list:
    if len(v.get('name')) == the_most_longest_name:
        result.append(v.get('name'))
# b
assert result == ['Denys']

all_ages = 0
for v in my_list:
    all_ages += v.get('age')

print(all_ages / len(my_list))

'''
5) Дано два словники my_dict_1 і my_dict_2.
а) Створити список із ключів, які є в обох словниках.
б) Створити список із ключів, які є у першому, але немає у другому словнику.
в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.

'''
my_dict_1 = {1: 11, 2: 22}
my_dict_2 = {1: 11, 3: 33}
result = []

for k, v in my_dict_1.items():
    if my_dict_2.get(k):
        result.append(k)
# a
assert result == [1]

result = []
for k, v in my_dict_1.items():
    if not my_dict_2.get(k):
        result.append(k)
# b
assert result == [2]

result = {}

for k, v in my_dict_1.items():
    if my_dict_2.get(k):
        result[k] = v
# c
assert result == {1: 11}

'''
г) Об'єднати ці два словники у новий словник за правилом:
якщо ключ є тільки в одному з двох словників - помістити пару ключ: значення,
якщо ключ є у двох словниках - помістити пару {ключ: [значення_з_першого_словника, значення_з_другого_словника]},

{1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
'''
my_dict_1 = {1: 1, 2: 2}
my_dict_2 = {11: 11, 2: 22}
result = {}
for k, v in my_dict_1.items():
    if not my_dict_2.get(k):
        result[k] = v
    else:
        if not result.get(k):
            result[k] = v
        else:
            old = result[k]
            result[k] = [old, v]

for k, v in my_dict_2.items():
    if not my_dict_1.get(k):
        result[k] = v
    else:
        if not result.get(k):
            result[k] = v
        else:
            old = result[k]
            result[k] = [old, v]

assert result == {1: 1, 11: 11, 2: [2, 22]}
