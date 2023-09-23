string=input("Input string: ")

#String Length
print(len(string))

#Index string
first_letter = string[0]
print(first_letter)
second_letter = string[1]
print(second_letter)
third_letter = string[2]
print(third_letter)

#Negative Indexing
print(string[-2])


#while looping with strings
print("while looping with strings")
index=0
while index<len(string):
    print(index, string[index])
    index=index+1
    
#For looping with strings
print("For looping with strings")
for i in string:
    print(i)


#Counting letters
print("Counting letters")
count=0
for i in string:
    if i =="a":
        count=count+1
print(count)

#Slicing Strings
print("Slicing strings")
string="Slicing strings"
print(string[0:4])  #Index 4 is not included in the string, up to but not including
print(string[2:8])

#Starting to end slicing
print(string[6:])
print(string[:3])

