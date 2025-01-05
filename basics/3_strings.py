#Methods of String
#String manipulation
#help(str)

sample_txt = "This is a sample string in double qoutes"
sample_txt2 ='This is a sample string in single qoutes'

#upper and lower 
print(sample_txt.upper())  #return the value in uppercase
print(sample_txt2.lower())

#replace
print(sample_txt.replace("n", "o")) #no count argument only replaces the first occurence
job_title = "Data Analyst"
print(job_title.replace("a","4", 3)) #last argument count replaces the number of occurences as specified

#split --> splits the string to a list
#sep looks for the provided char and splits it there; maxsplit delimits the split count with an initial index of 0
splitted = sample_txt.split(" ", 7)
print(splitted)

###Dunder methods or magic met"hods
print("Data ".__add__("Analyst"))
print(not str.__contains__("Data Analyst", "o"))

#string operation 
ftxt = "Jessie " + "Cudiamat"
print(ftxt)

mul_txt = "J" * 5
print(mul_txt)

sample_length = len(sample_txt) #counts the characters of a string including whitespaces
print(sample_length)







