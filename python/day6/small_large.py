a=eval(input("Enter your list= "))
l=a[0]
s=a[0]
for i in a:
    if s>i:
        s=i
    if l<i:
        l=i
print(f"Largest element in the list= {l}")
print(f"Smallest element in the list= {s}")