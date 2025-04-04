"""
Напишите функцию **`is_sorted(lst)`**, которая проверяет, является ли список чисел отсортированным по возрастанию.

**Требования:**

- Функция должна принимать один аргумент: список **`lst`**.
- Верните **`True`**, если список отсортирован, иначе — **`False`**.

**Пример:**

print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted([1, 3, 2, 4, 5]))  # False
"""

def is_sorted(lst):
    result = lst == sorted(lst)
    return result

print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted([1, 3, 2, 4, 5]))  # False