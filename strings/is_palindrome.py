"""
Напишите функцию **`is_palindrome(s)`**, которая проверяет, является ли строка палиндромом (читается одинаково слева направо и справа налево). Игнорируйте пробелы, знаки препинания и регистр.

**Требования:**

- Функция должна принимать один аргумент: строку **`s`**.
- Верните **`True`**, если строка является палиндромом, иначе — **`False`**.

**Пример:**

is_palindrome("A man, a plan, a canal: Panama")  # True

is_palindrome("racecar")                         # True

is_palindrome("hello")                           # False
"""


def is_palindrome(string):
    string = string.replace(" ", "").replace(",", "").replace(":", "").lower()
    string_revers = string[::-1]
    return string == string_revers


print(is_palindrome("A man, a plan, a canal: Panama"))  # True

print(is_palindrome("racecar"))  # True

print(is_palindrome("hello"))  # False
