n = int(input("enter the last number: "))
for i in range(1, n+1):
    print(i)
print(f"Even numbers between 1 to {n}")
for i in range(2,n):
    if(i%2==0):
        print(i)
print(f"Odd number between 1 to {n}")
for i in range(1,n):
    if(i%2!=0):
        print(i)