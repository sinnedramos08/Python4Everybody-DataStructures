'''
Open the file mbox-short.txt and read it line by line. When you find a 
line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second 
word in the line (i.e. the entire address of the person who sent the message). 
Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. 
Also look at the last line of the sample output to see how to print the count.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
'''

fh=open(r"C:\Users\denni\OneDrive\Desktop\Coding\Python\Coursera\Python4Everybody-DataStructures\Files\mbox.txt")
count=0

for line in fh:
    if "From" in line:
        line=line.rstrip()
        words=line.split(" ")
        if len(words)==8:
            print(words[1])
            count+=1

print(f"There were {count} lines in the file with From as the first word")

