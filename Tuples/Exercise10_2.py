'''
Write a program to read through the mbox-short.txt and figure out 
the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time 
and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, 
sorted by hour as shown below.
'''

fh=open(r"C:\Users\denni\OneDrive\Desktop\Coding\Python\Coursera\Python4Everybody-DataStructures\Tuples\mbox.txt")

words=[]
time=[]
hour={}
for lines in fh:
    if "From" in lines:
        lines=lines.rstrip()
        words=lines.split(" ")
        if len(words)==8:
            time_string=words[6]
            time=time_string.split(":")
            hour_string=time[0]
            hour[hour_string]=hour.get(hour_string,0)+1

#List comprehension
sorted_hour={key:val for key, val in sorted(hour.items())}

for v,k in sorted_hour.items():
    print(v, k)