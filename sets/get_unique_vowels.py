"""
Создайте функцию **`get_unique_vowels(s)`**, которая принимает строку и возвращает набор уникальных гласных, содержащихся в строке (игнорируя регистр).

**Требования:**

- Функция должна принимать один аргумент: строку **`s`**.
- Гласные буквы: **`a, e, i, o, u`**.
- Игнорируйте регистр символов.
- Верните множество уникальных гласных.

**Пример:**

print(get_unique_vowels("Hello World"))  # {'e', 'o'}
"""


def get_unique_vowels(s):
    s = s.lower()
    lst = ["a", "e", "i", "o", "u"]
    result = set()
    for letter in s:
        count_letter = s.count(letter)
        if count_letter == 1:
            if letter in lst:
                result.add(letter)
    return result


print(get_unique_vowels("Hello, Pier Dune!"))  # {'i', 'u', 'o'}
