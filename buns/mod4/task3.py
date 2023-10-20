def nod(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    else:
        man_n = max(a, b)
        min_n = min(a, b)
        return nod(man_n % min_n, min_n)

num1 = int(input())
num2 = int(input())
print(nod(num1, num2))

