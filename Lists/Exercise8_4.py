'''
Open the file romeo.txt and read it line by line. For each line, 
split the line into a list of words using the split() method. 
The program should build a list of words. For each word on each line 
check to see if the word is already in the list and if not append it 
to the list. When the program completes, sort and print the resulting words
in python sort() order as shown in the desired output.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
'''

filename=r"C:\Users\denni\OneDrive\Desktop\Coding\Python\Coursera\Python4Everybody-DataStructures\Lists\romeo.txt"
filehandle=open(filename)
lst=[]

for line in filehandle:
    words=line.split()
    for i in range(len(words)):
        if words[i] not in lst:
            lst.append(words[i])
print(lst)
lst.sort()
print(lst)