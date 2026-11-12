# Блок-схеми задач П3

Позначення за ГОСТ 19.701-90: овал — початок/кінець, паралелограм — ввід/вивід, прямокутник — дія, ромб — умова, прямокутник з подвійними боковими лініями — виклик підпрограми. Пунктир — повернення на початок циклу. У кожної схеми **один** блок «Кінець».

### Задача 1. c_to_f(c)

```mermaid
flowchart TD
    s(["Початок c_to_f(c)"])
    a["F = c · 9 / 5 + 32"]
    r["return F"]
    e(["Кінець"])
    s --> a
    a --> r
    r --> e
```

### Задача 2. triangle_area(a, h)

```mermaid
flowchart TD
    s(["Початок triangle_area(a, h)"])
    a["S = a · h / 2"]
    r["return S"]
    e(["Кінець"])
    s --> a
    a --> r
    r --> e
```

### Задача 3. min_max(a, b, c)

```mermaid
flowchart TD
    s(["Початок min_max(a, b, c)"])
    a["lo = min(a, b, c)<br/>hi = max(a, b, c)"]
    r["return lo, hi"]
    e(["Кінець"])
    s --> a
    a --> r
    r --> e
```

### Задача 4. is_prime(n)

```mermaid
flowchart TD
    s(["Початок is_prime(n)"])
    c1{"n < 2 ?"}
    f1["res = False"]
    i["res = True<br/>d = 2"]
    c2{"d · d ≤ n<br/>і res ?"}
    c3{"n % d == 0 ?"}
    f2["res = False"]
    inc["d = d + 1"]
    r["return res"]
    e(["Кінець"])
    s --> c1
    c1 -->|так| f1
    c1 -->|ні| i
    i --> c2
    c2 -->|так| c3
    c3 -->|так| f2
    c3 -->|ні| inc
    f2 --> inc
    inc -.-> c2
    c2 -->|ні| r
    f1 --> r
    r --> e
```

### Задача 4. primes_up_to(n) — процедура

```mermaid
flowchart TD
    s(["Початок primes_up_to(n)"])
    i["k = 2"]
    c{"k ≤ n ?"}
    sub[["is_prime(k)"]]
    c2{"просте?"}
    o[/"Вивести k (в рядок)"/]
    inc["k = k + 1"]
    nl[/"Перевести рядок"/]
    e(["Кінець"])
    s --> i
    i --> c
    c -->|так| sub
    sub --> c2
    c2 -->|так| o
    c2 -->|ні| inc
    o --> inc
    inc -.-> c
    c -->|ні| nl
    nl --> e
```

### Задача 5. print_box(width, symbol="*", height=3)

```mermaid
flowchart TD
    s(["Початок print_box"])
    o1[/"Вивести symbol · width"/]
    i["i = 1"]
    c{"i ≤ height − 2 ?"}
    o2[/"Вивести symbol +<br/>(width − 2) пробілів + symbol"/]
    inc["i = i + 1"]
    o3[/"Вивести symbol · width"/]
    e(["Кінець"])
    s --> o1
    o1 --> i
    i --> c
    c -->|так| o2
    o2 --> inc
    inc -.-> c
    c -->|ні| o3
    o3 --> e
```

### Задача 6. factorial_rec(n)

```mermaid
flowchart TD
    s(["Початок factorial_rec(n)"])
    c{"n ≤ 1 ?"}
    b["res = 1"]
    sub[["res = n · factorial_rec(n − 1)"]]
    r["return res"]
    e(["Кінець"])
    s --> c
    c -->|так| b
    c -->|ні| sub
    b --> r
    sub --> r
    r --> e
```

### Задача 6. fib_iter(n)

```mermaid
flowchart TD
    s(["Початок fib_iter(n)"])
    i["a, b = 0, 1<br/>i = 1"]
    c{"i ≤ n ?"}
    a["a, b = b, a + b"]
    inc["i = i + 1"]
    r["return a"]
    e(["Кінець"])
    s --> i
    i --> c
    c -->|так| a
    a --> inc
    inc -.-> c
    c -->|ні| r
    r --> e
```

### Задача 7. gcd(a, b) — алгоритм Евкліда

```mermaid
flowchart TD
    s(["Початок gcd(a, b)"])
    c{"b ≠ 0 ?"}
    a["a, b = b, a % b"]
    r["return a"]
    e(["Кінець"])
    s --> c
    c -->|так| a
    a -.-> c
    c -->|ні| r
    r --> e
```

### Задача 7. reduce_fraction(num, den)

```mermaid
flowchart TD
    s(["Початок reduce_fraction(num, den)"])
    sub[["g = gcd(num, den)"]]
    r["return num // g, den // g"]
    e(["Кінець"])
    s --> sub
    sub --> r
    r --> e
```

### Задача 8. digit_sum_rec(n)

```mermaid
flowchart TD
    s(["Початок digit_sum_rec(n)"])
    c{"n < 10 ?"}
    b["res = n"]
    sub[["res = n % 10 + digit_sum_rec(n // 10)"]]
    r["return res"]
    e(["Кінець"])
    s --> c
    c -->|так| b
    c -->|ні| sub
    b --> r
    sub --> r
    r --> e
```

### Задача 8. reverse_number(n)

```mermaid
flowchart TD
    s(["Початок reverse_number(n)"])
    i["r = 0"]
    c{"n > 0 ?"}
    a["r = r · 10 + n % 10<br/>n = n // 10"]
    ret["return r"]
    e(["Кінець"])
    s --> i
    i --> c
    c -->|так| a
    a -.-> c
    c -->|ні| ret
    ret --> e
```

### Задача 9. main() — меню

```mermaid
flowchart TD
    s(["Початок"])
    m[/"Показати меню,<br/>ввести choice"/]
    c0{"choice = 0 ?"}
    c1{"choice ∈ {1…5} ?"}
    w[/"Ввести числа"/]
    sub[["Виклик функції з mathtools"]]
    o[/"Вивести результат"/]
    u[/"«невідомий пункт меню»"/]
    e(["Кінець"])
    s --> m
    m --> c0
    c0 -->|так| e
    c0 -->|ні| c1
    c1 -->|так| w
    w --> sub
    sub --> o
    c1 -->|ні| u
    o -.-> m
    u -.-> m
```
