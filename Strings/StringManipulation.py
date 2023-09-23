string1= input("Input String 1: ")
string2= input("Input String 2: ")

#String Concatenation
string_concat= string1+" "+string2
print(string_concat)

#Using in as Logic operator
print("Dennis" in string1)

string_find="Dennis"
if string_find in string1:
    print(f"{string_find} found in string1")
else:
    print(f"{string_find} not found in string1")

#String Comparison
string_compar="dennis"
if string1 == string_compar:
    print(f"Your string, {string1}, is the same as {string_compar} ")
elif string1 < string_compar:
    print(f"Your string, {string1}, comes before {string_compar}")

elif string2 > string_compar:
    print(f"Your string, {string2}, comes after {string_compar}")

#Note, uppercase letters are less than lowercase letters

#String Library
string1_lowercase=string1.lower()
print(f"Your string lowercased is: {string1_lowercase}")

print("HI THERE".lower())

#Class String Methods
print("string 1 is of class",type(string1))

#Find operator, like in but returns the string index 
print("Find operator")
find_index = string1.find("en")
print(find_index, "\n") #If the return value is -1, therefore the strin is not found

#Search and replace operator
#Syntax: str.replace("string to find and to be replace", "string that will replace","number of replacements")
print("Search and replace operator \n")
string1_replaced= string1.replace("d","E",1)
print(string1_replaced, "\n")

#Stripping Whitespace
print("Stripping Whitespace \n")
print(string1.lstrip())
print(string1.rstrip())
print(string1.strip(), "\n")

#Startswith method, return true of false
print("Startswith method \n")
print(string1.startswith("d"))

