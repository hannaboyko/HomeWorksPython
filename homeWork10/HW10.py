"""
1. Написати функцію, яка отримує один параметр - ім'я директорії та повертає словник виду
{'filenames': [список файлів у папці], 'dirnames': [список усіх підпапок у папці]}.
Підпапки враховувати лише першого рівня вкладення. Папка в папці в папці - таке не брати))
"""
from pathlib import Path

def ls(path):
    filenames = []
    dirnames = []
    entries = Path(path)
    for entry in entries.iterdir():
        if entry.is_dir():
            dirnames.append(entry.name)
        elif entry.is_file():
            filenames.append(entry.name)
        else:
            continue
    return {'filenames': filenames, 'dirnames': dirnames}

print(ls('.'))

"""
2. Написати функцію, яка отримує два параметри – словник, описаний у пункті 1
і значення булю (True/False) - можна зробити за замовчуванням.
Функція повертає той самий словник, але з відсортованими іменами файлів та папок у відповідних списках.
Булеве значення True означає, що порядок сортування алфавітний, False – зворотний порядок.
"""
def sort(data, reverse=False):
    result = {}
    for k, v in data.items():
        result[k] = (sorted(v, reverse=reverse))
    return result


print(sort(ls('.')))
print(sort(ls('.'), reverse=True))

"""
3. Написати функцію, яка отримує два параметри - словник, описаний у пункті 1 та рядок, який може бути
або ім'ям файлу, або ім'ям папки. (У імені файлу має бути точка).
Залежно від того, що функція отримала (ім'я файлу або ім'я папки) – записати його у відповідний список
та повернути оновлений словник.
"""
def append(data, path):
    result = data.copy()
    if path.find('.') == -1:
        result.get('dirnames').append(path)
    else:
        result.get('filenames').append(path)
    return result

print(append(ls('.'), 'new_dir'))
print(append(ls('.'), 'new_file.txt'))
