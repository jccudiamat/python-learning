#value in string
#Your task is to write a program that:
#1)checks if a string is inside a list of strings
#2)outputs a confirmation message if it is

names = ["Mark Rober","Backyard Scientist","Vsauce"]

youtuber = "Mark Rober"

#using for loop
for name in names:
    if youtuber==name:
         print(f"{name} exists in the list {names} in index {names.index(name)}")
         break
    else:
         print(f"{youtuber} does not exist!")
         
#using if statement
if youtuber in names:
    print(f"{youtuber} exists in the list {names} in index {names.index(youtuber)}")
else:
    print(f"{youtuber} does not exist!")
   
#using ternary operator
res = "Youtuber exists" if youtuber in names else "Does not exist"
print(res)
