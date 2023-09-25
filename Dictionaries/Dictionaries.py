#Dictionaries
#'Bag' of values, each with its own label
#?Dictionary syntax: {'key': 'item'}

#Instatiate dictionary object
purse=dict()
purse['money']=12
purse['candy']=3
purse['tissue']=75
print(purse)

#Dictionary is mutable
print(purse['candy'])
purse['candy']=purse['candy']+2
print(purse['candy'])

#Appending on dictionary
#Just add new key and value to dictionary instead of using
#append method
purse["clothes"]=24
print(purse)
