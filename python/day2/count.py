a=input("Enter a string: ")
#length of string
print("length of string=",len(a))
#count of vowels
c=0
for i in a:
    if i.lower() in "aeiou":
        c+=1
print("number of vowels=",c)
#count the words
w=a.split()
print(w)
print("number of words=",len(w))
#count the consonants
c=0
for i in a:
    if i.isalpha() and i.lower() not in "aeiou":
        c+=1
print("number of consonants=",c)