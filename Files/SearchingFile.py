handle=open(r"C:\Users\denni\OneDrive\Desktop\Coding\Python\Coursera\Python4Everybody-DataStructures\Files\mbox.txt")

for line in handle:
    if line.startswith("From: "):
        if "@uct.ac.za" in line:
            print(line,end="")