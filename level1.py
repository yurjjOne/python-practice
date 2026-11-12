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


# Задача 4. Прості числа
def is_prime(n):
    """True, якщо n просте; дільники перебираємо до кореня з n."""
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


def primes_up_to(n):
    """Процедура: друкує прості числа від 2 до n в один рядок."""
    for k in range(2, n + 1):
        if is_prime(k):
            print(k, end=" ")
    print()


def count_primes(n):
    """Кількість простих чисел від 2 до n (спробуйте самі)."""
    count = 0
    for k in range(2, n + 1):
        if is_prime(k):
            count += 1
    return count


# Задача 5. Рамка
def print_box(width, symbol="*", height=3):
    """Процедура: порожня рамка шириною width.

    height=3 — додатковий параметр зі значенням за замовчуванням
    (спробуйте самі): висота рамки в рядках, мінімум 2.
    """
    print(symbol * width)
    for _ in range(height - 2):
        print(symbol + " " * (width - 2) + symbol)
    print(symbol * width)


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

    # Задача 4
    print(is_prime(0), is_prime(1), "очікуємо False False")
    print(is_prime(2), "очікуємо True")
    print(is_prime(9), is_prime(15), "очікуємо False False")
    print(is_prime(17), is_prime(29), "очікуємо True True")
    primes_up_to(30)          # 2 3 5 7 11 13 17 19 23 29
    print(count_primes(20), "очікуємо 8")

    # Задача 5
    print_box(4)
    print_box(3, "#")
    print_box(6)
    print_box(5, "#", 4)
