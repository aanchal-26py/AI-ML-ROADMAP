a=eval(input("Enter your list="))
b=int(input("enter the element to check="))
count=0
for i in a:
    if b==i:
        count += 1
print(f"Number appears {count} times")