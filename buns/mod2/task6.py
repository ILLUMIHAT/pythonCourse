site = input()

lenNum3 = 0
lenNum2 = 0
counterDomains = 0
for char in site:
    if char == '.':
        counterDomains += 1
    if counterDomains == 0:
        lenNum3 += 1
    elif counterDomains == 1:
        lenNum2 += 1
thirdDomain = site[:lenNum3]
secondDomain = site[lenNum3 + 1: lenNum3 + lenNum2]
firstDomain = site[lenNum2 + lenNum3 + 1:]
print(firstDomain)
print(secondDomain)
print(thirdDomain)