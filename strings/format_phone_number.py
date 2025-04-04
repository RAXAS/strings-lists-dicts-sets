"""
Напишите функцию **`format_phone_number(digits)`**, которая принимает строку из 10 цифр и возвращает её в формате **`(XXX) XXX-XXXX`**.

**Требования:**

- Функция должна принимать один аргумент: строку **`digits`**.
- Верните отформатированный номер телефона.

**Пример:**

print(format_phone_number("1234567890"))  # "(123) 456-7890”
"""

def format_phone_number(digits):
    result = "(" + digits[0:3] + ") " + digits[3:6] + "-" + digits[6:10]
    return result

print(format_phone_number("1234567890"))