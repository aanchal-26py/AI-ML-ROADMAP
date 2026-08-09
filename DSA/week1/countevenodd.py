n=int(input("Enter length of array="))
a=[]
even=0
odd=0
for i in range(n):
    value=int(input(f"Enter list element {i+1}="))
    a.append(value)
    if (value%2==0):
        even += 1
    else:
        odd += 1
print("Your list=",a)
print("even no. in list=",even)
print("odd no. in list=",odd)