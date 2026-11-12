"""Меню для бібліотеки mathtools."""
from mathtools import gcd, lcm, is_prime, factorial, divide, power

MENU = """
1 — НСД і НСК
2 — просте число?
3 — факторіал
4 — ділення
5 — степінь
0 — вихід"""


def main():
    while True:
        print(MENU)
        choice = input("Ваш вибір: ")
        if choice == "0":
            print("вихід")
            break
        elif choice == "1":
            a = int(input("a = "))
            b = int(input("b = "))
            print("НСД =", gcd(a, b), "НСК =", lcm(a, b))
        elif choice == "2":
            n = int(input("n = "))
            if is_prime(n):
                print("просте")
            else:
                print("складене")
        elif choice == "3":
            n = int(input("n = "))
            print(factorial(n))
        elif choice == "4":
            a = float(input("a = "))
            b = float(input("b = "))
            result = divide(a, b)
            if result is None:
                print("ділити на нуль не можна")
            else:
                print(result)
        elif choice == "5":
            x = float(input("x = "))
            n = int(input("n = "))
            print(power(x, n))
        else:
            print("невідомий пункт меню")


if __name__ == "__main__":
    main()
