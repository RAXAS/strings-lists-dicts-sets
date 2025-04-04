"""
Напишите функцию **`remove_duplicates(s)`**, которая принимает строку и возвращает новую строку, из которой удалены все повторяющиеся символы, оставляя только первое вхождение каждого символа.

**Требования:**

- Функция должна принимать один аргумент: строку **`s`**.
- Верните строку без повторяющихся символов.

**Пример:**

remove_duplicates("programming")  # "progamin”
"""

def remove_duplicates(string):
    result = ""
    for letter in string:
        if letter not in result:
            result += letter

    return result

print(remove_duplicates("programming"))