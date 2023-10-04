line = input()

countOne = 0
countZero = 0

for char in line:
    if char == "1":
        countOne += 1
    else:
        countZero += 1
if countOne == countZero:
    print("yes")
else:
    print("no")