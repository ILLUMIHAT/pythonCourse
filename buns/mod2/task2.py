def round_number(number, n):
    multiplier = 10 ** n
    rounded_number = int(number * multiplier + 0.5) / multiplier
    rounded_number = str(rounded_number)
    counter = 0
    for char in rounded_number:
        if char == '.':
            if rounded_number[counter+1] == '0' and rounded_number[counter+1] == rounded_number[-1]:
                rounded_number += '0'
                break
        counter += 1
    return rounded_number

squareSideLength = float(input('Введите длину стороны квадрата \n'))
perimeterSquare = squareSideLength * 4
areaSquare = squareSideLength**2
diagonalSquare = squareSideLength * 2**0.5
print(round_number(perimeterSquare, 2), round_number(areaSquare, 2), round_number(diagonalSquare, 2))





