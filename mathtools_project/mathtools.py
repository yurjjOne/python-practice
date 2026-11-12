"""Бібліотека mathtools: лише обчислення, без input і print."""


def gcd(a, b):
    """Найбільший спільний дільник."""
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Найменше спільне кратне."""
    return a // gcd(a, b) * b


def is_prime(n):
    """True, якщо n — просте число."""
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


def factorial(n):
    """Факторіал n (рекурсивно)."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def divide(a, b):
    """Частка a / b; при діленні на нуль повертає None."""
    if b == 0:
        return None
    return a / b


def power(x, n=2):
    """Степінь x ** n; за замовчуванням — квадрат (спробуйте самі)."""
    return x ** n
