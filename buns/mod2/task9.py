line = input()
soglas = 'бвгджзйклмнпрстфхцчшщ'
glas = 'уеыаоэяию'
countGlas = 0
countSoglas = 0
for char in line:
    if char in soglas:
        countSoglas += 1
    elif char in glas:
        countGlas += 1
print(countGlas, countSoglas)