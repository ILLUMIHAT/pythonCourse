line = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
str_i = line[0]
number_n = int(line[2:])
index_i = 0
counter = 0
for char in alphabet:
    if char == str_i:
        index_i = counter
        break
    counter += 1
index_k = index_i + number_n
print(alphabet[index_k])