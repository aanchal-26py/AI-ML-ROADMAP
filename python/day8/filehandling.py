f=open("Intro.txt","w")
f.write("Hello\nMy name is Aanchal Sharma")
f.close()
with open("Intro.txt","r") as f:
    print(f.read())
with open("Intro.txt","a") as f:
    f.write("\nI am a btech 3rd year student")
with open("Intro.txt","r") as f:
    print(f.read())