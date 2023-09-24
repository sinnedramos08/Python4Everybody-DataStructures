#Opening the txt file
#Syntax: var_handle=open(filename, mode)
#use the whole path of the txt file to be accessed
#use r-string for the path because of the slashes
handle=open(r"C:\Users\denni\OneDrive\Desktop\Coding\Python\Coursera\Python4Everybody-DataStructures\Files\mbox.txt")

#Using this prints only info about the file and the handling type
#print(handle)
#print("\n")

#Use handle.read() to read the statements inside the file
print("Statements inside the file: \n")
storage=handle.read()
print(storage)

#Note, .read() will read through the file until the cursor reaches the end
#Because of this, there is nothing more to read from the file
#This makes sure that the cursor goes back to the beginning of the file
handle.seek(0)


#Using for loop to read the statements inside the file
#Note that using this method, new lines will be doubled
#for i in handle:
    #print(i)    

#Count how many lines
count=0
for i in handle:
    count=count+1
print(f"Number of lines: {count}")


