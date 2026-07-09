def count_vowels(a):
    c=0
    for i in a:
        if i.lower() in "aeiou":
            c=c+1
    return c
x=input("Enter word=")
print(f"total no of vowel= {count_vowels(x)}")