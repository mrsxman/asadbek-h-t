# 1
k = int(input('число: '))
n = int(input('сколько раз: '))
if n > 0:
    for i in range(n):
        print(k)
else:
    print('n больще 0')
# 2
a = int(input('число а: '))
b = int(input('число b: '))

for i in range(a, b + 1):
    print(i)

print(f'a = {a}, b = {b}')
print(f'chiqarilgan sonlar soni {b - a + 1}')

# 3
a = int(input('число a: '))
b = int(input('число b: '))

for i in range(b, a, - 1):
    print(i, end=" ")

print(f'chiqarilgan sonlar soni {b - a + 1}')

# 4
sum_ = int(input('цена кг конфет: '))
for i in range(1, 11):
    print(f'{i}kg стоит сум {i * sum_}')

#  5
sum_ = int(input('цена кг конфет: '))
price = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
for i in price:
    new_price = sum_ * i
    print(f"{i} kg konfet narxi: ${new_price:.2f}")

#  6
sum_ = int(input('цена кг конфет: '))
price = [1.2, 1.4, 1.6, 1.8, 2]
for i in price:
    new_price = sum_ * i
    print(f'{i} kg konfet narxi: {new_price}')

# 7
a = int(input('число: '))
b = int(input('число: '))
if a < b:
    total = 0
    for i in range(a, b + 1):
        total += i
        print(total)

# 8
a = int(input('число: '))
b = int(input('число: '))
if a < b:
    total = 1
    for i in range(a, b + 1):
        total *= i
        print(total)

#  9
a = int(input('число: '))
b = int(input('число: '))
if a < b:
    total = 0
    for i in range(a, b + 1):
        i = 2
        total += i
        print(total)

# 10
n = int(input('число: '))

if n <= 0:
    print("n должен быть больше 0")
else:
    S = 0
    for i in range(1, n + 1):
        S += 1 / i

    print(f"S = {S}")

#  11
n = int(input("число: "))

if n <= 0:
    print("n должен быть больше 0.")
else:
    S = 0
    for i in range(n, 2 * n + 1):
        S += i*2

    print(f"S = {S}")

#  12
n = int(input("число: "))

if n <= 0:
    print("n должен быть больше 0")
else:
    S = 1.0
    for i in range(1, n + 1):
        S *= 1.0 + i / 10.0

    print(f"S = {S}")

#  13
n = int(input("n butun sonini kiriting: "))

if n <= 0:
    print("Noto'g'ri kiritish. n musbat butun soni bo'lishi kerak.")
else:
    S = 0
    sign = 1
    for i in range(1, n + 1):
        S += sign * i / 10.0
        sign *= -1

    print(f"S = {S}")

#  14
n = int(input("n butun sonini kiriting: "))

if n <= 0:
    print("Noto'g'ri kiritish. n musbat butun soni bo'lishi kerak.")
else:
    result = 0
    for i in range(1, n + 1):
        result += (2 * i - 1)

    print(f"{n} gacha bo'lgan sonlar kvadratlari yig'indisi: {result}")

# 15
a = float(input("a haqiqiy sonini kiriting: "))
n = int(input("n butun sonini kiriting: "))

result = 1.0

for _ in range(n):
    result *= a

print(f"{a} ning {n}-darajasi: {result}")

# 16


n = int(input("n ni kiriting: "))

for i in range(1, n+1):
    daraja = i ** 2  # Bu o'rniga istalgan daraja ko'rsating
    print(f"{i}-chi daraja: {daraja}")

# 17

n = int(input("n ni kiriting: "))
a = float(input("a ni kiriting: "))

summa = 0

for i in range(1, n + 1):
    daraja = a ** i
    summa += daraja
    print(f"{a} ning {i}-chi darajasi: {daraja}")

print(f"Barcha darajalar yig'indisi: {summa}")



# 18

n = int(input("n ni kiriting: "))
a = float(input("a ni kiriting: "))

summa = 0
daraja = 1

for i in range(1, n + 1):
    daraja *= a
    summa += daraja
    print(f"{a} ning {i}-chi darajasi: {daraja}")

print(f"Barcha darajalar yig'indisi: {summa}")



# 19


n = int(input("n ni kiriting: "))

kopaytma = 1

for i in range(1, n + 1):
    kopaytma *= i
    print(f"{i}-chi sonning kopaytmasi: {kopaytma}")



# 20


n = int(input("n ni kiriting: "))

yigindi = 0

for i in range(1, n + 1):
    yigindi += i

print(f"Barcha sonlar yig'indisi: {yigindi}")


# 21

n = int(input("n ni kiriting: "))

yigindi = 0

for i in range(1, n + 1):
    yigindi += i**2

print(f"Barcha sonlar kvadrati yig'indisi: {yigindi}")


# 22


n = int(input("n ni kiriting: "))
x = float(input("x ni kiriting: "))

yigindi = 0

for i in range(1, n + 1):
    yigindi += x**i

print(f"Barcha darajalar yig'indisi: {yigindi}")


# 22

n = int(input("n ni kiriting: "))
x = float(input("x ni kiriting: "))

yigindi = 0

for i in range(1, n + 1):
    yigindi += x**i

print(f"Barcha darajalar yig'indisi: {yigindi}")

# 23


n = int(input("n ni kiriting (butun son): "))
x = float(input("x ni kiriting (haqiqiy son): "))

yigindi = 0

for i in range(1, n + 1):
    yigindi += x**i

print(f"Barcha darajalar yig'indisi: {yigindi}")


# 24


import math

n = int(input("n ni kiriting (butun son): "))
x = float(input("x ni kiriting (haqiqiy son): "))

yigindi = 0

for i in range(n + 1):
    yigindi += math.pow(x, i) / math.factorial(i)

print(f"Natijasi (cox({x})): {yigindi}")


# 25

n = int(input("n ni kiriting (butun son, n > 0): "))
x = float(input("x ni kiriting (haqiqiy son, |x| < 1): "))

if n <= 0 or abs(x) >= 1:
    print("Shartlar bajarilmadi. n > 0, |x| < 1 bo'lishi kerak.")
else:
    yigindi = 0

    for i in range(n + 1):
        yigindi += x**i

    print(f"Natijasi: {yigindi}")




# 26



n = int(input("n ni kiriting (butun son, n > 0): "))
x = float(input("x ni kiriting (haqiqiy son, |x| < 1): "))

if n <= 0 or abs(x) >= 1:
    print("Shartlar bajarilmadi. n > 0, |x| < 1 bo'lishi kerak.")
else:
    yigindi = 0

    for i in range(n + 1):
        yigindi += x**i

    print(f"Natijasi: {yigindi}")


# 27

import math

n = int(input("n butun sonini kiriting (n > 0): "))
x = float(input("|x| < 1 bo'lishi kerak, x ni kiriting: "))

if n <= 0 or abs(x) >= 1:
    print("Noto'g'ri kiritish. n > 0 va |x| < 1 bo'lishi kerak.")
else:
    total = x
    term = 1

    for i in range(1, n + 1):
        term *= (2 * i - 1) * x / ((2 * i) * (2 * i + 1))
        total += term

    print(f"Yig'indi: {total}")

#28
import math

n = int(input("n butun sonini kiriting (n > 0): "))
x = float(input("|x| < 1 bo'lishi kerak, x ni kiriting: "))

if n <= 0 or abs(x) >= 1:
    print("Noto'g'ri kiritish. n > 0 va |x| < 1 bo'lishi kerak.")
else:
    total = 1
    term = 1

    for i in range(1, n + 1):
        term *= ((-1)  (i - 1)) * (2 * i - 1) * x / math.prod(range(2, 2 * i + 1, 2))
        total += term

    print(f"Yig'indi: {total}")

# 29
A = float(input("A ni kiriting: "))
B = float(input("B ni kiriting: "))
n = int(input("n ni kiriting: "))

if n < 0:
    print("Noto'g'ri kiritish. n musbat bo'lishi kerak.")
else:
    interval = B - A
    step = interval / n

    print(f'["[{A}, {B}|"] kesmada {n} ta kesma bor:')
    for i in range(n):
        start_point = A + i * step
        end_point = A + (i + 1) * step
        print(f'[{start_point}, {end_point}]')

# 30
import math

A = float(input("A ni kiriting: "))
B = float(input("B ni kiriting: "))
n = int(input("n ni kiriting: "))

if n < 1:
    print("Noto'g'ri kiritish. n 1 dan katta bo'lishi kerak.")
else:
    interval = B - A
    step = interval / n

    print(f'["[{A}, {B}]"] kesmada {n} ta kesma bor:')
    for i in range(n + 1):
        x = A + i * step
        f_x = 1 - math.sin(x)
        print(f'F({x}) = {f_x}')

#31
n = int(input("n butun sonini kiriting: "))

A = 2  # dastlabki qiymat
for k in range(1, n + 1):
    print(f"A{k} = {A}")
    A = 2 + 1 / A

#32
n = int(input("n butun sonini kiriting: "))

A = 1  # dastlabki qiymat
for k in range(1, n + 1):
    print(f"A{k} = {A}")
    A = (A + 1) / k

#33
n = int(input("n butun sonini kiriting (n > 1): "))

if n <= 1:
    print("Noto'g'ri kiritish. n 1 dan katta bo'lishi kerak.")
else:
    fib_sequence = [1, 1]

    for k in range(3, n + 1):
        fk = fib_sequence[-2] + fib_sequence[-1]
        fib_sequence.append(fk)

    print(f"Fibonacci ketma-ketlikning dastlabki {n} ta hadlari:")
    for i, fk in enumerate(fib_sequence, start=1):
        print(f"F{i} = {fk}")

#34
n = int(input("n butun sonini kiriting (n > 1): "))

if n <= 1:
    print("Noto'g'ri kiritish. n 1 dan katta bo'lishi kerak.")
else:
    A_sequence = [1, 2]

    for k in range(3, n + 1):
        Ak = (A_sequence[-2] + 2 * A_sequence[-1]) / 3
        A_sequence.append(Ak)

    print(f"Ketma-ketlikning dastlabki {n} ta hadlari:")
    for i, Ak in enumerate(A_sequence, start=1):
        print(f"A{i} = {Ak}")

# 35
n = int(input("n butun sonini kiriting (n > 2): "))

if n <= 2:
    print("Noto'g'ri kiritish. n 2 dan katta bo'lishi kerak.")
else:
    A_sequence = [1, 2, 3]

    for k in range(4, n + 1):
        Ak = A_sequence[-1] + A_sequence[-2] - 2 * A_sequence[-3]
        A_sequence.append(Ak)

    print(f"Ketma-ketlikning dastlabki {n} ta hadlari:")
    for i, Ak in enumerate(A_sequence, start=1):
        print(f"A{i} = {Ak}")
