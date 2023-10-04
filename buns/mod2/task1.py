numbers = input('Введите два числа через запятую \n')
first = 0
second = 0
counter = 0
for char in numbers:
    if char == ',':
        first = int(numbers[:counter])
        second = int(numbers[counter + 2:])
    counter += 1
print(first % second)
