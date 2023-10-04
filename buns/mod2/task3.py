numbers = input()
num1 = 0
num2 = 0
num3 = 0
len_num1 = 0
len_num2 = 0
spaceCounter = 0

for char in numbers:
    if char == ' ':
        spaceCounter += 1
    if spaceCounter == 0:
        len_num1 += 1
    elif spaceCounter == 1:
        len_num2 += 1

num1 = int(numbers[:len_num1])
num2 = int(numbers[len_num1 + 1: len_num1 + len_num2])
num3 = int(numbers[len_num2 + len_num1 + 1:])

if (num1 >= num2 and num1 <= num3) or (num1 >= num3 and num1 <= num2):
    print(num1)
elif (num2 >= num1 and num2 <= num3) or (num2 >= num3 and num2 <= num1):
    print(num2)
else:
    print(num3)

