#Conditionals: if Statements
#if statements use bool (Boolean) values (True or False) to decide whether or not to execute code. If
#the comparison x > y is True , the interpreter runs the indented block.

#x = int(input("What's x? "))
#y = int(input("What's y? "))

#if x < y:
#    print("x is less than y")

#If we further revise the code to this (a series of if statements), then the first if statement is
#evaluated, followed by the second and finally the last if statement runs its evaluation. This flow
#of decisions is called Control Flow.

#x = int(input("What's x? "))
#y = int(input("What's y? "))

#if x < y:
#    print("x is less than y")

#if x > y:
#    print("x is greater than y")

#if x == y:
#    print("x is equal to y")

#This program can be further improved by not asking 3 consecutive questions. Afterall, not all
# statements can be true. 
#Elif statement. The use of elif allows the program to make less decisions which improves the
#speed of the program.

#x = int(input("What's x? "))
#y = int(input("What's y? "))

#if x < y:
#    print("x is less than y")

#elif x > y:
#    print("x is greater than y")

#elif x == y:
#    print("x is equal to y")

#Else statement. Notice that the elif x == y statement is not necessary logically. Final improvement.
#We create a "catch all" default outcome using an else statement.

#x = int(input("What's x? "))
#y = int(input("What's y? "))

#if x < y:
#    print("x is less than y")

#elif x > y:
#    print("x is greater than y")

#else:
#    print("x is equal to y")

#or allows your program to decide between one or more alternatives. For example

#x = int(input("What's x? "))
#y = int(input("what's y? "))

#if x > y or x < y:
#    print("x is not equal to y")

#else:
#    print("x is equal to y")

#The outcome of the program is the same but complexity has reduced and efficiency has increased.
#We can remove the or entirely and simply ask "Is x not equal to y?", using x != y

#x = int(input("What's x? "))
#y = int(input("What's y? "))

#if x != y:
#    print("x is not equal to y")

#else:
#    print("x is equal to y")

#We could also use this statement x == y

x = int(input("What's x? "))
y = int(input("What's y? "))

if x == y:
    print("x is equal to y")

else:
    print("x is not equal to y")