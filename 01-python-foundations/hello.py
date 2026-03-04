#Ask for the name
name=input("What is your name? ")

#Ask for the age
age=int (input("How old are you? "))

#Ask where user lives
country=input("Where do you live? ")

#Display the answers and the different string/output features

#Printing Hello and the inputted name using +
print("Hello, " + name)

#Using a comma to pass in multiple arguments. In this case passing text plus the variable "age". You
#can use commas to pass multiple arguments.
print("You are",age,"years old")

"""The print function automatically includes the end='\n'. This \n indicates that the print function 
 will automatically create a line break when run. The function takes an argument called end, and the
 default is to create a new line. However, we can technically provide an argument for end ourselves
 such that a new line is not created.
"""
print("Oh really! You live in ", end="")
print(country,"??""That sucks! ")