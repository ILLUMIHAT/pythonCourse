size = int(input())

for col in range(1, size+1):
    for row in range(1, size+1):
        if row != size:
            print(row, end=", ")
        else:
            print(row)

print()

for col in range(1, size+1):
    for row in range(1, size+1):
        if row != size:
            print(col, end=", ")
        else:
            print(col)
