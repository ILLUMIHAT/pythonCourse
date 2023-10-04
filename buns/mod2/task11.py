line = input()
point = False
a = ""
for char in line:
    if char == " ":
        continue
    elif char in a:
        point = True
        break
    a += char
print(point)