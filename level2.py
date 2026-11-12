"""Практична робота П3. Рівень 2 — задачі 6–8.

Автор: Михайлюк Юрій, група МІТ-1026г
"""


# Задача 6. Факторіал і Фібоначчі двома способами
def factorial_iter(n):
    """n! циклом."""
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result


def factorial_rec(n):
    """n! рекурсією: база n <= 1."""
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)


def fib_iter(n):
    """n-те число Фібоначчі циклом (F0 = 0, F1 = 1)."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_rec(n):
    """n-те число Фібоначчі рекурсією: база n < 2."""
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)
# Чому fib_rec повільна: кожен виклик двічі викликає саму себе, тому кількість
# викликів росте майже як 1.6 ** n. Ті самі значення (fib_rec(2), fib_rec(3)...)
# рахуються тисячі разів, а fib_iter рахує кожне число лише один раз.


# Задача 7. НСД, НСК і дроби
def gcd(a, b):
    """Найбільший спільний дільник (алгоритм Евкліда)."""
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Найменше спільне кратне; викликає gcd."""
    return a // gcd(a, b) * b


def is_coprime(a, b):
    """True, якщо НСД(a, b) = 1."""
    return gcd(a, b) == 1


def reduce_fraction(num, den):
    """Скорочений дріб: пара (чисельник, знаменник)."""
    g = gcd(num, den)
    return num // g, den // g


# Задача 8. Цифри числа
def digit_sum_rec(n):
    """Сума цифр рекурсією: база — одна цифра."""
    if n < 10:
        return n
    return n % 10 + digit_sum_rec(n // 10)


def reverse_number(n):
    """Число навпаки: 1230 -> 321."""
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n //= 10
    return r


def is_palindrome_number(n):
    """True, якщо число читається однаково в обидва боки."""
    return n == reverse_number(n)


if __name__ == "__main__":
    import time

    # Задача 6
    for n in range(0, 11):
        assert factorial_iter(n) == factorial_rec(n)
    print("factorial_iter == factorial_rec для n = 0..10")
    print(factorial_iter(0), factorial_rec(5), factorial_iter(10))  # 1 120 3628800
    print(fib_iter(0), fib_iter(1), fib_iter(7))                    # 0 1 13
    print(fib_iter(10), fib_rec(10), fib_iter(20))                  # 55 55 6765

    for n in (30, 35):
        start = time.perf_counter()
        value = fib_rec(n)
        print("fib_rec(%d) = %d, час %.2f с" % (n, value, time.perf_counter() - start))
    start = time.perf_counter()
    value = fib_iter(35)
    print("fib_iter(35) = %d, час %.6f с" % (value, time.perf_counter() - start))

    # Задача 7
    print(gcd(12, 18), lcm(12, 18), lcm(4, 6))                      # 6 36 12
    print(is_coprime(7, 13), is_coprime(8, 9))                      # True True
    print(is_coprime(12, 18), is_coprime(8, 12))                    # False False
    print(reduce_fraction(12, 18), reduce_fraction(10, 25), reduce_fraction(7, 13))

    # Задача 8
    print(digit_sum_rec(7), digit_sum_rec(10), digit_sum_rec(50525), digit_sum_rec(999))
    print(reverse_number(1230), reverse_number(5072))               # 321 2705
    print(is_palindrome_number(12321), is_palindrome_number(1221), is_palindrome_number(7))
    print(is_palindrome_number(1234), is_palindrome_number(10))     # False False
