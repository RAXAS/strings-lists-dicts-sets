"""
Напишите функцию **`longest_word(s)`**, которая возвращает самое длинное слово в строке.

**Требования:**

- Функция должна принимать один аргумент: строку **`s`**.
- Верните самое длинное слово.

**Пример:**

longest_word("In the middle of a vast desert, an extraordinary adventure awaits")  # "extraordinary”
"""


def longest_word(string):
    result = ""
    string = string.replace(",", "").split(" ")
    for word in string:
        if len(word) > len(result):
            result = word
    return f"{result}"


print(longest_word("In the middle of a vast desert, an extraordinary adventure awaits"))
