#Concatenating list using "+"
a=[0,1,2,3,4,5,6,7,8]
b=[9,10,11,12,13,14,15,16,17]
c=a+b
print(c)

#Slicing List
print(c[0:8])
print(c[:])
print(c[4:])
print(c[:10])

#List is an object that has methods
example_list=list()
print(type(example_list))
#print(dir(example_list))

#Method: append("element")
example_list.append("nice")
example_list.append("one")
example_list.append("dennis")
print(example_list)

# in operator
print(9 in example_list)
print("nice" in example_list)

#Using other list methods
numlist=[]
while True:
    inp=input("Enter a Number: ")
    if inp == "done": break
    value=float(inp)
    numlist.append(value)

average=sum(numlist)/len(numlist)
print(numlist)
print(average)