'''Number Guessing Game 🎮

Requirements:

Computer chooses a secret number (1–10).
User keeps guessing.
Print:
"Too High"
"Too Low"
"Correct!"'''
print("guess the number(1-10)")
n=int(input("Enter your number="))
while n!=7:
    print("1.try again\n2.exit")
    c=int(input("="))
    if c==2:
        break
    else:
        print("Hint",end=":")
        if n>0 and n<=5:
            print("TOO LOW")
        elif n>=9:
            print("TOO HIGH")
        else:
            print("TOO closee...")
        n=int(input("Enter your number="))
print("The number is 7")
print("Thankyou!!")