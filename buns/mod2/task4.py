number = int(input())

def bin(decimal_num):
    binary_num = ""
    while decimal_num > 0:
        remains = decimal_num % 2
        binary_num = str(remains) + binary_num
        decimal_num = decimal_num // 2
    return binary_num

def oct(decimal_num):
    octal_num = ""
    while decimal_num > 0:
        remains = decimal_num % 8
        octal_num = str(remains) + octal_num
        decimal_num = decimal_num // 8
    return octal_num

def hex(decimal_num):
    hex_num = ''
    while decimal_num != 0:
        remains = decimal_num % 16
        if remains < 10:
            hex_num += str(remains)
        else:
            if remains == 10:
                hex_num += 'A'
            elif remains == 11:
                hex_num += 'B'
            elif remains == 12:
                hex_num += 'C'
            elif remains == 13:
                hex_num += 'D'
            elif remains == 14:
                hex_num += 'E'
            else:
                hex_num += 'F'
        decimal_num = decimal_num // 16
    return hex_num[::-1]

print(bin(number) + ", " + oct(number) + ", " + hex(number))