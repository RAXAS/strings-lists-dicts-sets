"""
Напишите функцию **`dict_to_lists(my_dict)`**, которая принимает словарь и возвращает два списка: один с ключами и другой с соответствующими значениями.

**Требования:**

- Функция должна принимать один аргумент: словарь **`my_dict`**.
- Используйте методы **`.keys()`** и **`.values()`** для извлечения ключей и значений.
- Верните кортеж, содержащий два списка: список ключей и список значений.

**Пример:**

my_dict = {"a": 1, "b": 2, "c": 3}
print(dict_to_lists(my_dict))  # (["a", "b", "c"], [1, 2, 3])
"""


def dict_to_lists(my_dict):
    keys = []
    values = []
    for key, value in my_dict.items():
        keys.append(key)
        values.append(value)
    return keys, values


my_dict = {"a": 1, "b": 2, "c": 3}
print(dict_to_lists(my_dict))  # (["a", "b", "c"], [1, 2, 3])
