line = input()
newWord = ""
lastLetter = ""

for char in line:
    if char == ' ':
        if lastLetter:
            newWord += lastLetter
        lastLetter = ""
    else:
        lastLetter = char
if lastLetter:
    newWord += lastLetter

print(newWord)
