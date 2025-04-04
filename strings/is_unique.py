"""
Напишите функцию **`is_unique(s)`**, которая проверяет, содержит ли заданная строка все уникальные символы (без повторов).

**Требования:**

- Функция должна принимать один аргумент: строку **`s`**.
- Верните **`True`**, если все символы уникальны, иначе — **`False`**.

**Пример:**

is_unique("abcdef")  # True
is_unique("hello")  # False
"""


def is_unique(string):
    set_string = set(string)
    result = len(string) == len(set_string)
    return result


print(is_unique("abcdef"))  # True
print(is_unique("hello"))  # False
