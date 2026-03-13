#match - similar to if, elif and else statements, match statements can be used to conditionally run code
#that matches certain values.

#name = input("What's your name? ")
#if name == "Harry":
#    print("Griffyndor")
#elif name == "Hermoine":
#    print("Griffyndor")
#elif name == "Ron":
#    print("Griffyndor")
#elif name =="Draco":
#    print("Slytherin")
#else:
#    print("Who?")

#The first three conditional statements print the same response.
#We can improve this code slightly with the use of the or keyword.

#name = input("What's your name? ")
#if name == "Harry" or name == "Hermoine" or name == "Ron":
#    print("Griffyndor")

#elif name == "Draco":
#    print("Slytherin")

#else:
#    print("Who?")

#Alternatively, we can use match statements to map names to houses

#name = input("What's your name? ")

#match name:
#    case "Harry":
#        print("Griffyndor")
#    case "Hermoine":
#        print("Griffyndor")
#    case "Ron":
#        print("griffyndor")
#    case "Draco":
#        print("Slytherin")
#    case _:
#        print("Who?")

#Notice the use of the _ symbol in the last case. This will match with any input resulting in similar
#behaviour as an else statement.
#A match statement compares the value following the match keyword with each of the values following the
#case keywords. In the event a match is found, the respective indented code section is executed, and the
#program stops the matching. We can improve the code.

name = input("What's your name? ")
match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Griffyndor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")