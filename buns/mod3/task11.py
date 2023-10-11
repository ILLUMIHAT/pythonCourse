def Cross_Zero(str1,str2, str3):
    board = [str1, str2, str3]

    for stroke in board:
        if stroke[0] == stroke[1] and stroke[0] == stroke[2] and (stroke[0] == "X" or stroke[0] == "O"):
            return stroke[0]

    for i in range(len(board)):
        if str1[i] == str2[i] and str1[i] == str3[i] and (str3[i] == "O" or str3[i] == "X"):
            return str1[i]

    if str1[0] == str2[1] and str2[1] == str3[2] and (str3[2] == "O" or str3[2] == "X"):
        return str1[0]
    elif str1[2] == str2[1] and str2[1] == str3[0] and (str3[0] == "O" or str3[0] == "X"):
        return str1[2]
    else:
        return "Ничья"

str1 = input()
str2 = input()
str3 = input()
print(Cross_Zero(str1, str2, str3))