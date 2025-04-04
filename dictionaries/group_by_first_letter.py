"""
Напишите функцию **`group_by_first_letter(strings)`**, которая принимает список строк и группирует их в словарь, где ключами являются первые символы строк, а значением — список строк, начинающихся с этого символа.

**Требования:**

- Функция должна принимать один аргумент: список строк **`strings`**.
- Верните словарь с группировкой.

**Пример:**

strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings))
# {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}
"""


def group_by_first_letter(strings):
    result = {}
    for word in strings:
        key = word[0]
        if key not in result:
            result[key] = []
        result[key].append(word)
    return result


strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings))
# {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}
