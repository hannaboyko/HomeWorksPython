'''
1) У вас є список my_list із значеннями типу int. Роздрукувати значення, які більше 100.
   Завдання виконати за допомогою циклу for.

2) У вас є список my_list зі значеннями типу int і порожній список my_results. Додати в my_results ті значення,
   які більше 100. Роздрукувати список my_results. Завдання виконати за допомогою циклу for.

3) У вас є список my_list із значеннями типу int. Якщо my_list кількість елементів менше 2,
   то в кінець додати значення 0. Якщо кількість елементів більша або дорівнює 2,
   то додати суму останніх двох елементів. Кількість елементів у списку можна отримати за допомогою функції len(my_list)
'''

# 1
my_list = [1, 2, 3, 4, 100, 101, 200, 3000, 5]
for i in my_list:
    if i > 100:
        print(i)

# 2
my_list = [1, 2, 3, 4, 101, 200, 3000, 5]
my_results = []
for i in my_list:
    if i > 100:
        my_results.append(i)
for i in my_results:
    print(i)

# 3
my_list_1 = [1]
my_list_2 = [1, 2]
my_list_3 = [1, 2, 3]


def my_sum(arr):
    if arr:
        _result = arr.copy()
        if len(arr) < 2:
            _result.append(0)
        else:
            _result.append(_result[-1] + _result[-2])
        return _result


print(*my_sum(my_list_1))
print(*my_sum(my_list_2))
print(*my_sum(my_list_3))
