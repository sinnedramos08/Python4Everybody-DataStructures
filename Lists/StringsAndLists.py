# split() method for strings
# split a string into different words
sample_string="Hi, my name is Dennis Ramos"
split_sample_string=sample_string.split()
print(split_sample_string)

#parameter for split() is the delimiter
sample_string ="Hi;my;name;is;Dennis;Ramos"
split_sample_string=sample_string.split(";")
print(split_sample_string)

#Double Split Pattern
string_data = "From drramos3@up.edu.ph Sat Jan 5 09:15:16 2023"
split_string_data=string_data.split()
email_data=split_string_data[1]
print(email_data)
split_email_data=email_data.split("@")
print(split_email_data)