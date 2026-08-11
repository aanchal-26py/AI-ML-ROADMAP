length=int(input("Enter length of array="))
a=[]
maximum=0
for i in range(length):
    n=int(input(f"Enter {i+1} element of array="))
    a.append(n)
    if a[i]>maximum:
        maximum=a[i]
print("Largest element of array=",maximum)