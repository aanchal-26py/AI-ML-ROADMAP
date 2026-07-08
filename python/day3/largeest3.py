x=int(input("Enter first number="))
b=int(input("Enter second number="))
c=int(input("Enter third number="))
#first method
if b>x:
    x=b
if c>x:
    x=c
print("Largest number is=",x)
#second method
if b>x:
    if c>x:
        print("Largest number is=",c)
    else:
        print("Largest number is=",b)
else:
    if c>x:
        print("Largest number is=",c)
    else:
        print("Largest number is=",x)

    