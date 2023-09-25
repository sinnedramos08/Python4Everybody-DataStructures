#Using the names.txt file which has names in random order and frequency
#Create a program that will count the number of times each name appears in the
#names.txt file

fh=open(r"C:\Users\denni\OneDrive\Desktop\Coding\Python\Coursera\Python4Everybody-DataStructures\Dictionaries\Names.txt")


name_counter={}

for line in fh:
    line=line.rstrip()
    #If the name does not exist yet in dictionary
    #Add the name to the dictionary then make it 1
    if line not in name_counter:
        name_counter[line]=1
    #If the name aldready exists in the dictioanry then
    #Just add 1 for every instance it appears in the text
    else:
        name_counter[line]=name_counter[line]+1

print(name_counter)
dennis_frequency=name_counter['Dennis']
print(f"Name Dennis occured {dennis_frequency} times")
andrew_frequency=name_counter['Andrew']
print(f"Name Andrew occured {andrew_frequency} times")
ramos_frequency=name_counter['Ramos']
print(f"Name Ramos occured {ramos_frequency} times")


#Using get() method of dictionary
#Syntax: get("key", "default value")
#get() method returns the value of the key if it exists
#if it does not exist, key will be added to the dictionary
#with the value equal to the value set in the parameter

fh.seek(0) #Restart the 'cursor' in file
name_counter2={}

for line in fh:
    line=line.rstrip()
    name_counter2[line] =name_counter2.get(line,0)+1 #Note here that dictionary is mutable that is why it did not traceback

print(name_counter2)

#Makes a list of all the keys in the dictionary
print(list(name_counter2))
print(name_counter2.keys())

#Makes list of all the values in the dictionary
print(name_counter2.values())

#Makes a key value pair from the dictionary
print(name_counter2.items())

