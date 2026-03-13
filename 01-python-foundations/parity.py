#In mathematics, parity refers to whether a number is even or odd. The modulo, %, operator allows
#one to see if two numbers divide evenly or divide and have a remainder. E.g. 4%2==0 and 3%2!=0

#x = int(input("What's x? "))

#if x % 2 == 0:
#    print("Even")

#else:
#    print("Odd")

#Creating our own Parity Function

#def main():
#    x = int(input("What's x? "))
#    if is_even(x):
#       print("Even")
#    else:
#        print("Odd")

#def is_even(n):
#    if n % 2 == 0:
#        return True
#    else:
#        return False
#main()

#Notice that our if statement is_even(x) works even though there is no operator there. This is because
#our function returns a bool (Boolean) True or False, back to the main function. The if statement 
#simply evaluates whether or not is_even of x is true or false. Remember that if statements use bool
#values to decide whether or not to execute code. If the comparison n%2==0 is True, the interpreter
#runs the indented block.
#The return values here are bool values.
#Our function is_even is being used in the main function on line 16 if is_even(x): to make a decision.
#I'm using a function call as my boolean expression and it's ok because that function is_even returns
# True or it returns False and that's all I need in a conditional to make a decision to print even or
#to print odd.

# Pythonic - Ways to program that are sometimes only seen in Python.

#def main():
#    x = int(input("What's x? "))
#    if is_even(x):
#        print("Even")
#    else:
#        print("Odd")

#def is_even(n):
#    return True if n % 2 == 0 else False

#main()

#Notice that this return statement in our code is almost like a sentence in English. This is unique way
#of coding only seen in Python   
#We can further revise our code and make it more readable:

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print ("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0

main()

#Notice that the program will evaluate what is happening within the n % 2 == 0 as either True or False
#and simply return that to the main function. In this last iteration of the code, we only need to return n % 2 == 0 because this 
#expression is already boolean in itself i.e. it only has two possible outcomes, True or False. Is n divided by two having a 
#remainder of zero or not? If n % 2 == 0 then True if not then False. We can also encapsulate this expression into brackets.
