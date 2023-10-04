line = input()
str_s = line[:-2]
symbol_i = line[-1]
count_i = 0
for char in str_s:
    if char == symbol_i:
        count_i += 1
    else:
        break
print(count_i)