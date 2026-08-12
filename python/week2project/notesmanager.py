def createfile():
    with open("Notes.txt","w") as f:
        data=input("Enter=")
        f.write(data)
        print("Data added")
def viewnotes():
    with open("Notes.txt","r") as f:
        print(f.read())
def addnotes():
    with open("Notes.txt","a") as f:
        data=input("Enter=")
        f.write(data)
        print("Data added")
c=0
while c!=3:
    print('''===== NOTES =====
1. Add Note
2. View Notes
3. Exit''')
    c=int(input("="))
    try:
        if c==1:
            addnotes()
        elif c==2:
            viewnotes()
    except FileNotFoundError:
        print("File does not exist")
        s=input("You want to create new file=(y/n)=")
        if s=='y':
            createfile()
print("Thankyou!!")