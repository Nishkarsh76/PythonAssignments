string = input("Enter String: ")
lines=len(string)

i=1
spaces=(lines-1)
letter=1

while i<=lines:
    print(" "*(spaces),end="")
    spaces=spaces-1
    str=string[0:letter]
    letter=letter+1
    print(str)
    i=i+1
else:
    print("Pattern Printed")