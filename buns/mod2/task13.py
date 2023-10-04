barcode = input()
correctBarcode = ""
oddNmbers = 0
evenNumbers = 0
i = 1
for char in barcode:
    if i % 2 == 1:
        oddNmbers += int(char)
    else:
        evenNumbers += int(char)
    i += 1

sum = str(oddNmbers + (3 * evenNumbers))

if sum[-1] == "0":
    print("yes")
else:
    print("no")