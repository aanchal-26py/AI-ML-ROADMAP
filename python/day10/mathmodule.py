import math
try:
    a=float(input("Enter your no.="))
except:
    print("Invalid input")
else:
    print(f"Square of {a}={math.pow(a,2)}")
    print(f"Sqareroot of {a}={math.sqrt(a)}")
    print(f"Ceiling of {a}={math.ceil(a)}")
    print(f"Floor of {a}={math.floor(a)}")