number = input()
values = "+0123456789"
correctNumber = ""
for char in number:
    if char in values:
        correctNumber += char
print(correctNumber)
