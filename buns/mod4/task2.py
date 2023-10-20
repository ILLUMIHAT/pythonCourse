def fast_pow(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    if n < 0:
        return 1 / fast_pow(a, abs(n))
    if n % 2 == 0:
        return fast_pow((a ** 2), n/2)
    elif n % 2 == 1:
        return fast_pow(a, n-1) * a
a = int(input("Введите число "))
n = int(input("Введите степень "))
print(fast_pow(a, n))