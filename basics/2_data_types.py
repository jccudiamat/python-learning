#Data types
#Use help() function to learn methods 

total_salary = 110000
bonus_salary = 10000
##Check data type
print(type(total_salary))

base_salary = total_salary - bonus_salary
print(base_salary)

##TEXT
#str --> String
job_title = 'Data Analyst'
remove_word = 'Data'
#help(str)

fname = "data"
lname = "scientist"
fullname = fname + lname
print(fullname.capitalize())

##NUMERIC
#int --> 42
job_id = int(3.14)
print(job_id)
print(type(job_id))

#float --> 3.14

#complex --> 1 + 2j

##SEQUENCE
#list --> [1,2,3]

#tuple --> {1,2,3}

#range --> range(10)

##MAPPING
#dict --> {"key": "value"}

##SET
#set --> {1,2,3}

#frozenset --> frozenset({1,2,3})

##BOOLEAN
#bool --> True or False

##BINARY
#bytes --> b"Data"

#bytearray --> bytearray(5)

#memoryview --> memory(b"Data")





