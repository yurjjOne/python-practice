"""Практична робота П3. Рівень 1 — задачі 1–5.

Автор: Михайлюк Юрій, група МІТ-1026г
"""


# Задача 1. Температура
def c_to_f(c):
    """Цельсій -> Фаренгейт: F = C * 9 / 5 + 32."""
    return c * 9 / 5 + 32


def f_to_c(f):
    """Обернена функція (спробуйте самі): Фаренгейт -> Цельсій."""
    return (f - 32) * 5 / 9


# Задача 2. Площа трикутника
def triangle_area(a, h):
    """Площа трикутника за основою a і висотою h."""
    return a * h / 2


def rectangle_area(a, b):
    """Площа прямокутника (спробуйте самі)."""
    return a * b


# Задача 3. Мінімум і максимум
def min_max(a, b, c):
    """Пара (мінімум, максимум) з трьох чисел."""
    return min(a, b, c), max(a, b, c)


def min_max_if(a, b, c):
    """Те саме без вбудованих min і max — через if (спробуйте самі)."""
    lo = a
    hi = a
    if b < lo:
        lo = b
    if c < lo:
        lo = c
    if b > hi:
        hi = b
    if c > hi:
        hi = c
    return lo, hi


if __name__ == "__main__":
    # Задача 1
    print(c_to_f(100), "очікуємо 212.0")
    print(c_to_f(-40), "очікуємо -40.0")
    print(c_to_f(0), "очікуємо 32.0")
    print(round(c_to_f(37), 1), "очікуємо 98.6")
    print(round(f_to_c(c_to_f(25)), 6), "очікуємо 25.0")

    # Задача 2
    print(triangle_area(6, 4), "очікуємо 12.0")
    print(triangle_area(10, 3), "очікуємо 15.0")
    print(triangle_area(7, 2), "очікуємо 7.0")
    print(rectangle_area(3, 5), "очікуємо 15")

    # Задача 3
    lo, hi = min_max(4, 9, 2)
    print(lo, hi, "очікуємо 2 9")
    print(min_max(-5, -2, -9), "очікуємо (-9, -2)")
    print(min_max(3, 3, 3), "очікуємо (3, 3)")
    print(min_max_if(4, 9, 2), "очікуємо (2, 9)")
