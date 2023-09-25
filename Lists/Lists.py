#Lists are surrounded by square brackets
#Elements in the list are separated by comma
#An element can be a list also
#List can be empty
#List is mutable- meaning can be modified using index
first_list=['red','orange','yellow','green','blue']
print(first_list)

#For looping a list
for i in first_list:
    print(i)

#Index in list
print(first_list[0])
print(first_list[1])
print(first_list[2])

#Changing values using index operators
first_list[0] = "violet"
print(first_list)

#Range(start,stop (excluding the value),step) , returns a list 
#of numbers that range from
#zero to one less than the parameter
range_list=range(1,4,1)
for i in range_list:
    print(i)

# i in range ...
# note that range needs a number parameter
for j in range(len(first_list)):
    color=first_list[j]
    print(f"Color: {color}")