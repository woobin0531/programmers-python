str = input()
result = ""

for char in str:
    if char.islower():
        result += char.upper()
    elif char.isupper():
        result += char.lower()
    else:
      result += char
        
print(result)
