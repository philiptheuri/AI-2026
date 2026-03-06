#Creating our own Functions using the hello.py code
#Def

#Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
#name = input("What's your name? ").strip().title()

#Print the output
#print(f"Hello, {name}")

#Let's create a function that says "hello" for us.
name = input("What's your name? ")
hello()
print(name)
#This code brings an error because the hello funtion is not defined.

#Creating our own function that says hello
def hello():
    print("Hello")

name = input("What's your name? ")    