import mycalculator
try:
    a=int(input("Enter first value="))
    b=int(input("Enter second value="))
except ValueError:
    print("Invalid input")
else:
    print("add=",mycalculator.add(a,b))
    print("subtarct=",mycalculator.subtract(a,b))
    print("divide=",mycalculator.divide(a,b))
    print("multiply=",mycalculator.multiply(a,b))