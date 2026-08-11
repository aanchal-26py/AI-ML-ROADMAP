with open("Intro.txt","r") as f:
    content=f.read()
with open("Copyfile.txt","w") as f:
    f.write(content)
with open("Copyfile.txt","r") as f:
    print(f.read())