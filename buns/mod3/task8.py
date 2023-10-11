str = input().replace(" ", "-").replace("(", "-").replace(")", "-").split("-")
print("".join(str))