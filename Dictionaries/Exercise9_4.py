'''
Write a program to read through the mbox-short.txt and figure 
out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second 
word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's 
mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the 
dictionary using a maximum loop to find the most prolific committer.
'''

fh = open(r"C:\Users\denni\OneDrive\Desktop\Coding\Python\Coursera\Python4Everybody-DataStructures\Files\mbox.txt")

words=[]
histogram={}
#Make a histogram of all the email senders
for lines in fh:
    lines=lines.rstrip()
    if "From" in lines:
        print(lines)
        words=lines.split(" ")
        if len(words)==8:
            words_email=words[1]
            histogram[words_email]=histogram.get(words_email,0)+1

#print(histogram)

#Make a biggest count identifier
largest_key=None
largest_count=None
for key,value in histogram.items():
    if largest_count is None or int(value)>largest_count:
        largest_key=key
        largest_count=value

print(largest_key,largest_count)
        



    
