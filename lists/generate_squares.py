"""
Напишите функцию **`generate_squares(n)`**, которая генерирует список квадратов чисел от 1 до **`n`**.

**Требования:**

- Функция должна принимать один аргумент: число **`n`**.
- Верните список квадратов.

**Пример:**

print(generate_squares(5))  # [1, 4, 9, 16, 25]
"""


def generate_squares(n):
    result = [x ** 2 for x in range(1, n + 1)]
    return result


print(generate_squares(5))  # [1, 4, 9, 16, 25]
