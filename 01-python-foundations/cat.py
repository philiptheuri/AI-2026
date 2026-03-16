#Loops.
#Essentially, loops are a way to do things over and over again. Loops enable you to create a block of code that executes over and over
#again.

#print("Meow")
#print("Meow")
#print("Meow")

#while is a construct that allows me to ask a question again and again and everytime that we have seen a question, it's in the form of
#a boolean expression. A question to which the answer is True or False. How can i print out "meow" three times and ask three times
# a question to which the answer is True or False?

#i = 3
#while i != 0:
#    print("meow")
#    i = i - 1
#This will endlessy print "meow". If you don't change the value of i, its always 3, it's going to loop forever. This is an accidental 
#infinite loop. Ctrl + C breaks the loop
#We can also rework the logic of this program to

#i = 1
#while i <= 3:
#    print("meow")
#    i = i + 1
#For the statement i = i + 1, remember that the equal sign is our assignment operator from right to left. Logically it seems strange,
#how can i be equal to itself plus 1? Well it doesn't, until you execute this code from right to left. You add or subtract 1 from i
#and then you update the value of i on the left. The assignment copies the value from the right to the left.
#Let's now start counting from zero instead of one. For this we change the logic in the while loop from while i <= 3, to while i < 3.
#This allows the program to still print 3 meows without running through the number 3. The loop stops at 2 i.e. 0,1,2.

#i = 0
#while i < 3:
#    print("meow")
#    i = i + 1

#Now to tighten up i = i + 1

#i = 0
#while i < 3:
#    print("meow")
#    i += 1

#For Loops. A For loop is a different type of loop. A For loop iterates through a list of items. A list is a variable in Python.

#for i in[0,1,2]:
#    print("meow")

#In this code, i will be automatically initialized to 0, then meow will be printed, then 1, meow, then 2, meow and because those are
#all the values in the list, python will automatically stop. So our list is [0,1,2] This code is not efficient however if we have
# a large list. The easiest way to correct this in python is to use a function called range.

#for i in range(3):
#    print("meow")

#Our code can be further improved. Notice how we never use i explicitly in our code.That is, while Python needs the i as a place to store
#the number of the iteration of the loop, we never use it for any other purpose. In Python, if such a variable does not have any other
#significance in our code, we can simply represent this variable as a single underscore _ as follows (This is pythonic):

#for _ in range(3):
#    print("meow")

#To explore further possibilities
#print("meow" * 3)

#This program produces meowmeowmeow. Let's consider a line break
#print("meow\n" * 3,end="")

#Notice how this code produces 3 meows, each on a separate line. By adding end="" and the \n we tell the interpreter to add a line break
#at the end of each meow.

#Improving with user input.
#Perhaps we want input from a user. We can use loops as a way of validating the input of the user.
#A common paradigm in Python is to use a while loop to validate the input of the user. For example, let's try prompting the user for a 
#number greater than or equal to 0.
#Starting with the "while True:" statement immediately induces an infinite loop (a loop that goes on forever).

#while True:
#    n = int(input("What's n? "))
#    if n < 0:
#        continue
#    else:
#        break

#continue explicitly tells Python to go to the next iteration of a loop.
#break tells Python to "break out" of loop early before it has finished all of its iterations. In this case we'll continue to the next
#iteration of the loop when n is less than 0- ultimately reprompting the user with "What's n?". If though, n is greater than or equal
# 0, we'll break out of the loop and allow the rest of our program to run.
#It turns out that continue is redundant in this code. We can improve this program as follows:

#while True:
#    n = int(input("What's n? "))
#    if n > 0:
#        break
#for _ in range(n):
#    print("meow")

#Notice how this while loop will always run (forever) until n is greater than 0. When n is greater than 0, the loop breaks.

#We can use functions to further improve our code.

#def main():
#    meow(get_number())

#def get_number():
#    while True:
#        n = int(input("What's n? "))
#        if n > 0:
#            return n
        
#def meow(n):
#    for _ in range(n):
#        print("meow")

#main()

#Notice how not only did we change our code to operate in multiple functions, but we also used a return statement to return a
#value of n back to the main faunction. The return statement can be inside the loop or outside of the loop but within the function.
