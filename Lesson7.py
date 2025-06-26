char = str(input("Put a charater(s): "))
if len(char) != 1:
    print("Plz write a character only")
else:
    print(ord(char))