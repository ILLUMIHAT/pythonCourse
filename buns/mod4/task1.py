def check_numbers(numbers):
    uniqueNum = set(numbers)

    if len(uniqueNum) == 1:
        return "Все числа равны"

    if len(uniqueNum) == len(numbers):
        return "Все числа разные"

    else:
        return "Есть равные и неравные числа"

numbers = input("Введите список чисел через пробел ").split()
print(check_numbers(numbers))



