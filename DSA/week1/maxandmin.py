a=eval(input("Enter your list="))
max=a[0]
min=a[0]
for i in a:
    if max<i:
        max=i
    if min>i:
        min = i
print(f"maximum element in list={max}")
print(f"minimum element in list={min}")