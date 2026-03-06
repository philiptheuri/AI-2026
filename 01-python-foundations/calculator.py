#Simple Calculator
#x = 1
#y = 2
#z = x + y
#print (z)

#Making this more interactive using the input function. This results in a wrong answer because your
#your input from the keyboard on your computer comes into the interpreter as text, it is treated as
#a string and is concatenated using the + sign
#x = input("What's x? ")
#y = input("What's y? ")
#z = x + y
#print(z)

#Correct version of the code is as follows. The use of int(x) is called "casting" where a value of a
#variable is temporarily changed from one type to another. In this case from str to int.
#x = input("What's x? ")
#y = input("What's y? ")
#z = int (x) + int (y)
#print (z)

#We can further improve our code as follows:
#x = int(input("What's x? "))
#y = int(input("What's y? "))
#Output. Two ways based on what I have learnt.
#print(x+y)
#print(f"The result is {x+y}")
#This illustrates that you can run functions on functions. The inner function, input(), is run first
#and then the outer one is run, int().

#Float Basics
#x = float(input("What's x? "))
#y = float(input("What's y? "))
#print (x + y)

#To round off to the nearest integer use the round() function. On Python documentation for round
#you'll see the available arguments for round are round(number[, ndigits]). Those square brackets
#indicate that something optional can be specified by the programmer. Therefore, you could do
#round(n) to round a digit to its nearest integer. Alternatively, you could code as follows:

#Get user input
#x = float(input("What's x? "))
#y = float(input("What's y? "))

#Create a rounded result
#z = round(x + y)

#Print the result. The output will be to the nearest integer.
#print(z)

#How to format the output of long numbers. For example, rather than seeing 1000, you wish to see 1,000

#Get User input
#x = float(input("What's x? "))
#y = float(input("What's y? "))

#Create a rounded result
#z = round(x + y)

#Print the formatted result. f"{z:,}" creates a scenario where the outputted z will include commas
#print(f"{z:,}")

#How can we round floating point values when for example x = 2 and y = 3 and the result z is 
#0.66666666 seemingly going to infinity?

#Get user input
#x = float(input("What's x? "))
#y = float(input("What's y? "))

#Calculate the result
#z = x / y

#Print the result
#print(z)

#Lets imagine that we want to round this down

#Get the user's input
#x = float(input("What's x? "))
#y = float(input("What's y? "))

#Calculate the result and round
#z = round(x / y, 2)

#Print the result. This rounds off to the nearest 2 decimal points.
#print (z)

#We could use an f-string to format the output as follows.

#Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

#Calculate the result
z = x / y

#Print the result. This cryptic f-string code displays as our prior rounding strategy. 
print(f"{z:.2f}")






