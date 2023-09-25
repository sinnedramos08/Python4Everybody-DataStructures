#Tuples are immutable list

#assign 2 variables using tuples
(x,y)=(4,5)
print(x)
print(y)

#comparing tuples
#compar values from left to right
print((0,1,2)<(-1,6,7))

#sorting with tuples
sample_dict={"a":111, "b":222, "c":3,}
#Sort the dictionary by key
print(sorted(sample_dict.items()))

#Sort dictionary by value
tmp=list()

for k,v in sample_dict.items():
    tmp.append((v,k)) #Note here that v became the first value of the tuple instead of k

print(tmp)

tmp=sorted(tmp, reverse=True) 
print(tmp)

#Using .sort() method
#This method does not return any values
sample_list=(45,23,57,1243,5344)
print(sample_list[3])