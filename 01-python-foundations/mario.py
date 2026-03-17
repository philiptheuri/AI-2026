#print("#")
#print("#")
#print("#")

#for _ in range(3):
#    print("#")

#Lets create a function for this and provide a bit more abstraction whereby an abstraction is a simplification of a more complicated
#idea. Main does not need to know the underlying implementation of print_column

#def main():
#    print_column(3)


#def print_column(height):
#    for _ in range(height):
#        print("#")

#main()

#Notice how our column can grow as much as we want without any hard coding. Now, lets try to print a row horizontally. Modify your code
#as follows:

#def main():
#    print_row(4)

#def print_row(width):
#    print("?" * width)
    
#main()

#How could we implement both rows and columns within our code?
#def main():
#    print_square(3)

#def print_square(size):

    #For each row in square
#    for i in range(size):

        #For each brick in row
#        for j in range(size):

            #Print brick
#            print("#", end="")

        #Print blank line. Happens when you call print like this.
#        print()

#main()

#Notice that we have an outer loop that addresses each row in the square. Then, we have an inner loop that prints a brick in each row.
#Finally we have a print statement that prints a blank line.

#We can further abstract away our code:
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)


main()

