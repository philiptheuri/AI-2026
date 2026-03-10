#In mathematics, parity refers to whether a number is even or odd. The modulo, %, operator allows
#one to see if two numbers divide evenly or divide and have a remainder. E.g. 4%2==0 and 3%2!=0

#x = int(input("What's x? "))

#if x % 2 == 0:
#    print("Even")

#else:
#    print("Odd")

#Creating our own Parity Function

def main():
    x = int(input("What's x? "))
    if x % 2 == 0:
        print("Even")
    else:
        print("False")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
main()

#Notice that our if statement is_even(x) works even though there is no operator there. This is because
#our function returns a bool (Boolean) True or False, back to the main function. The if statement 
#simply evaluates whether or not is_even of x is true or false. Remember that if statements use bool
#values to decide whether or not to execute code. If the comparison n%2==0 is True, the interpreter
#runs the indented block.