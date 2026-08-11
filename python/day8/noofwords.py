with open("Intro.txt","r") as f:
    c=0
    for i in f.readlines():
        for j in i.split():
            c=c+1
print(f"Total no. of words={c}")