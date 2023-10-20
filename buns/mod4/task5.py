input_file = input("Ведите имя файла ")
with open(input_file, 'r', encoding='UTF-8') as file:
    n = file.read()
dictionary = []
for char in set(n):
    if char.isalpha():
        dictionary.append([n.count(char), char])
dictionary.sort()
with open('output.txt', 'w', encoding='UTF-8') as file:
    for pair in dictionary:
        file.write(f"{pair[1]}: {pair[0]}\n")