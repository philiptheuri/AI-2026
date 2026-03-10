#Creating our own Functions using the hello.py code
#Def

#Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
#name = input("What's your name? ").strip().title()

#Print the output
#print(f"Hello, {name}")

#Let's create a function that says "hello" for us.
#name = input("What's your name? ")
#hello()
#print(name)
#This code brings an error because the hello funtion is not defined.

#Creating our own function that says hello, or anything that you define in the function. 
#Notice that everything under def hello is indented. Python is an indented language. It uses
#indentation to understand what is part of the above function. Therefore everything in the hello
#function must be indented. When something is not indented, it treats it as if it is not inside the
#hello function.
#def hello():
#    print("Hello")

#name = input("What's your name? ")
#hello()
#print(name)

#We can further improve our code

#Create a function. Here, we are creating the function hello but we are telling the interpreter that
#this function takes a single parameter: a variable called "to". Therefore when you call hello(name),
#the computer passes name into the hello function as "to". This is how we pass values into functions.
#The output is now closer to our ideal presented earlier.

#def hello(to):
#    print("hello,",to)

#Output using our own function
#name = input("What's your name? ")

#hello(name)

#The "name" variable is passed as an argument/input to the hello function.Even though the variable
#is called "name" here, when the function itself is called, the computer assumes that the same value
#is now called "to". So name is essentially copied to another variable called "to", so that in the
#context of hello I can say hello "to" that variable instead.


#We can change our code to add a default value to hello.
#The first hello will behave as you might expect, and the second hello, which is not passed a value
#will, by default, output hello world.

#Create our own function
#def hello(to = "world"):
#    print("Hello,",to)

#Output using our own function
#name = input("What's your name? ")
#hello(name)

#Output without expected arguments
#hello()

#Main Function - Main part of the program/ code
#We don't have to have our function at the start of our program. We can move it down, but we need to 
#tell our interpreter that we have a main function and a separate hello function.

#def main():
    #Output using our own function
#    name = input("What's your name? ")
#    hello(name)

    #Output without passing the expected arguments
#    hello()

#Creating our own function
#def hello(to = "world"):
#    print ("Hello,",to)

#This will create an error of some sorts. If we run the code, nothing happens. The reason for this
#is that nothing in this code is actually calling the main function and bringing our program to life.
#The following small modification will call the main function and restore our program to working
#order.
#Name is being passed from the main function to the hello function and once it's passed it is 
#called "to" which is fine because it's completely up to each individual function to name its own
#variables or name its own arguments. This is a way now I'm handing to the hello function the value
#of that variable so it can be printed by hello as well. 

def main():
    #Output using our own function
    name = input("What's your name? ")
    hello(name)

    #Output without passing the expected arguments
    hello()

#Creating our own function
def hello(to = "world"):
    print("Hello,",to)

main()

#Scope refers to a variable only existing in the context in which you defined it. So if you define a
#variable, name for example, in the main function only, then I can only use it in the main function
#and not the hello function, it doesn't exist in that so-called scope. 

#Returning Values. Go to calculator.py code