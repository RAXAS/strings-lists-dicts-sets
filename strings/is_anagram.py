"""
Напишите функцию **`is_anagram(s1, s2)`**, которая проверяет, являются ли две строки анаграммами (перестановками друг друга).

**Требования:**

- Функция должна принимать два аргумента: строки **`s1`** и **`s2`**.
- Игнорируйте регистр символов.
- Верните **`True`**, если строки являются анаграммами, иначе — **`False`**.

**Пример:**

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
"""


def is_anagram(word_1, word_2):
    word_1 = sorted(word_1.lower())
    word_2 = sorted(word_2.lower())
    result = word_1 == word_2
    return result


print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))  # False
