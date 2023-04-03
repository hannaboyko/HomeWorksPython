from datetime import datetime
"""
Всі пункти зробити як окремі функції та їх виклики.

1. Написати функцію, яка отримує як параметр ім'я файлу назви інтернет доменів (domains.txt)
та повертає їх у вигляді списку рядків (назви повертати без крапки).
"""
with open("domains.txt") as fp:
    for line in fp.readlines():
        print(line.replace('.', '').strip())
"""
2. Написати функцію, яка отримує як параметр ім'я файла (names.txt)
і повертає список усіх прізвищ із нього.
Кожен рядок файлу містить номер, прізвище, країну, кілька (таблиця взята з вікіпедії).
Розділювач - символ табуляції "t"
"""
with open("names.txt") as fp:
    for line in fp.readlines():
        surnames = line.split()
        print(surnames[1])
"""
3. Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
словників виду {"date": date}
у яких date - це дата з рядка (якщо є),
Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]
"""
result = []

with open("authors.txt") as fp:
    for line in fp.readlines():
        _d = line.split(' - ')
        if len(_d) > 1:
            _date = _d[0].rstrip()
            if _date:
                result.append({"date": _date})

print(result)

'''
4* (*здавати не обов'язково).
Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
словників виду {"date_original": date_original, "date_modified": date_modified}
у яких date_original - це дата з рядка (якщо є),
а date_modified - ця ж дата, представлена у форматі "dd/mm/yyyy" (d-день, m-місяць, y-рік)
Наприклад [{"date_original": "8th February 1828", "date_modified": 08/02/1828}, ...]
'''
result = []

def extract_int(s):
    return ''.join(c for c in s if c.isdigit())

DATE_FORMAT = '%d %B %Y'
DATE_FORMAT_TARGET = '%d/%m/%Y'

with open("authors.txt") as fp:
    for line in fp.readlines():
        _d = line.split(' - ')
        if len(_d) > 1:
            _date = _d[0].rstrip()
            if _date:
                _p = _date.split()
                if len(_p) == 3:
                    _p[0] = extract_int(_p[0])
                elif len(_p) == 2:
                    _p.insert(0, '1')
                else:
                    continue
                date_modified = datetime.strptime(" ".join(_p), DATE_FORMAT)
                result.append({"date_original": _date, "date_modified": date_modified.strftime(DATE_FORMAT_TARGET)})

print(result)
