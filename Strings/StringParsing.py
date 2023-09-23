#Finding, parsing, and extracting
print("Finding, parsing, and extracting \n")
string_data = "From drramos3@up.edu.ph Sat Jan 5 09:15:16 2023"
index_at=string_data.find("@")
print(f"@ character in index {index_at}")

#Second index parameter is where the find method will begin finding the 
# character/string
#Find method syntax: str.find("string", index start, index end)
index_space=string_data.find(" ", index_at) 
print(f"space character after @ in index {index_space}")

#Extract the host name from the data
host_name=string_data[index_at+1: index_space]
print(f"The host name is: {host_name}")