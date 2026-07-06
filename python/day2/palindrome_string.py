a=input("Enter word=")
if a==a[::-1]:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")
print("Reversed word=",a[::-1])