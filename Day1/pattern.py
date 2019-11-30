lines = int(input("Enter Number of Line: "))

i=1

while i<=lines:
    print("*"*i,end=" ")
    print(" ")
    i=i+1
else:
    print("Pattern Printed")

print("----------------")
i=lines
spaces=0
while i>=1:
    print("*"*i)
    i=i-1

else:
    print("Pattern Printed")


print("----------------")
i=lines
spaces=0
while i>=1:
    print(" "*(spaces),end="")
    spaces=spaces+1
    print("*"*i)
    i=i-1

else:
    print("Pattern Printed")

print("----------------")
i=1
spaces=(lines-1)

while i<=lines:
    print(" "*(spaces),end="")
    spaces=spaces-1
    print("*"*i)
    i=i+1
else:
    print("Pattern Printed")
print("----------------")
i=1
spaces=(lines-1)

while i<=lines:
    print(" "*(spaces),end="")
    spaces=spaces-1
    print("* "*i)
    i=i+1
else:
    print("Pattern Printed")