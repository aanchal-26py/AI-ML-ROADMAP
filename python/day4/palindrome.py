n=int(input("Enter the number="))
s=0
copy=n
while (n!=0):
    d=n%10
    s=s*10+d
    n=n//10
if copy==s:
    print("It is a Palindrome number")
else:
    print("It is not a palindrome number")