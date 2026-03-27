#Looping through a string
#text = "Hello World"
#for char in text:
#    print(char)

#Slicing a string i.e. extracting parts
#text = "I am going to master Strings"

#Print from index 0 to index 3 not including 3
#print(text[0:3])

#More ways to do it.
#Prints from index 6 to 11 not including index 11
#print(text[4:11])

#Prints from index 0 up to (not including) 5
#print(text[:5])

#Prints from index 12 not including 12
#print(text[12:])

#Prints index 5
#print(text[5])

#This is a list with 7 elements.
#numbers = [0,1,2,3,5,4,6]

#Prints number 3 which is the fourth element
#print(numbers[4])

#Counting characters including spaces, can be used in a str or a list.
#print(len(numbers))
#print(len(text))

#Negative indexing. This prints the last character.
#print(text[-1])

#Second last
#print(text[-2])

#Reversing a string using ::-1. [start:end:step] step = -1 --go backwards
#print(text[::-1])

#Reversing using a for loop
#text = "I am going to master Strings"
#reversed_text = ""

#for char in text:
#    reversed_text = char + reversed_text
#print(reversed_text)

#Count characters without len
#text = "I am going to master Strings"

#count = 0

#for char in text:
    #Only count real characters, not spaces. If char is not a space, then, count it.
#    if char != " ":
#        count += 1
#        print(count)


#text = "The sun is 93000000 kilometres away from earth."
#count = 0

#for char in text:
    #Ignore numbers and spaces using .isalpha(method)
#    if char.isalpha():
#        count += 1
#print(count)

#Practice test 1
#text = "Hello world how are you"
#count = 0

#Count the number of spaces in the text
#for char in text:
#    if char == " ":
#        count += 1

#print(count)

#Practice test 2
#text = "banana"
#count = 0

#Count the number of a's
#for char in text:
#    if char == "a":
#        count += 1
        
#print(count)

#Practice test 3
#text = "Hello World"
#count = 0

#Count number of uppercase letters
#for char in text:
#    if char.isupper():
#        count += 1

#print(count)

#Practice test 4
#text = "hello world!!!"
#result = ""

#for char in text:
#    #if CHAR is not inside this list. Only count real characters, not spaces.
#    if char not in [" ", "!"]:
#        result += char

#print(result)

#The strip() method removes spaces from the beginning and the end (edges only) but the spaces on the inside remain.
#text = "   Hello World   "
#print(text.strip())

#The lower() method (Normalize case) converts everything to lowercase
#print(text.strip().lower())

#The replace() method replaces one thing with another
#print(text.strip().lower().replace(" ", "..."))

#Use replace() to remove characters as well
#print(text.replace("H", ""))

#Note that strings do not change automatically. To change the string to all uppercase we do this:
#text = text.upper()
#print(text)

#Chaining methods
#pattern = "  clean split transform join  "
#cleaned = pattern.strip().lower().replace(" ", ">")
#print(cleaned)

#Build a cleaner function
#def main():
#    text = input("Put a string with numbers and letters: ")
#    clean = cleaned_text(text)
#    print(clean)

#def cleaned_text(t): #The parameter for the funtion definition doesn't have to be named like the parameter in the main hence t and text
#    t = t.strip()
#    t = t.lower()
#    t = t.replace("!", "").replace("@", "").replace("&", "").replace("$", "")
#    return t


#if __name__ == "__main__":
#    main()

#Day 3 str practice

#split() turns a str into a list which is a variable type in Python. split() removes spaces and separates words

#text = "I am going to split this str into a list of words"
#words = text.split() #text is split into a list
#print(words)

#" ".join() joins a list into a str. Key insight: " " the space is what goes between words. It can also be "...".join
#combined = " ".join(words)
#print(combined)
#new_combined = "...".join(words)
#print(new_combined)

#Example to fix messy spaces
#text = "God    is good, all     the time!"
#the_word = text.split()
#clean = " ".join(the_word)
#print(clean)

#Day 3 practice exercises
#split words, join words
#text = "I love Python"
#separated = text.split()
#combined = "...".join(separated)
#print (separated)
#print(combined)

#Fix messy spaces
#new_text = "hello    world    again"
#new_separated = new_text.split()
#clean_text = " ".join(new_separated)
#print(clean_text)

#Count words
#words = "I love data science"
#new_words = words.split()
#count = 0
#for char in new_words:
#    if char != " ":
#        count += 1
#print(count)

#Reverse word order
#motto = "I love Python"
#new_motto = motto.split()
#new_motto.reverse() #use reverse to reverse a list. Turn a str to a list then reverse it.
#clean_motto = " ".join(new_motto)
#print(clean_motto)


#Day 4 - Searching and Conditions

#"in" checks if something exists inside a str. Output is bool (True or False). Is this inside that?
#text = "hello world"
#print("hello" in text)
#print("world" in text)
#print("Hi" in text)

#Using "if" with "in"
#if "hello" in text:
#    print("Greeting detected")

#Case Problem. If we use "hello" instead of "Hello" in the "if" statement, the output will be nothing. We fix this using the lower()
#method. text is first converted to lower case and then the condition evaluates to True. If you normalize compare using the same format.
#text = "Hello World"
#if "hello" in text.lower():
#    print("Yes")

#Multiple conditions
#text = "hello world"
#if "hello" in text and "world" in text:
#    print("Both found")

#if "hello" in text or "hi" in text:
#    print("Greetings detected")

#startswith() and endswith() - used in detecting emails, filtering data, validating input, building smart systems
#print(text.startswith("hello"))
#print(text.endswith("world"))
#learn how to use startwith() and endswith() with conditionals as well as other ways to use the two methods

#Day 4 practice
#text = "I love Python"
#if "Python" in text:
#    print("Yes")

#if "python" in text.lower():
#    print("Yes")

#text = input("Say something: ")
#if "hi" in text or "hello" in text:
#    print("Greetings detected")
#else:
#    print("No greetings detected")

#text = input("Enter email: ")
#if "@" in text:
#    print("Valid")
#else:
#    print("Invalid")

#filename = "photo.jpg"
#if filename.endswith(".jpg"):
#    print("Image file")


#mini project: smart response system
#def main():
#    user_input = input("You: ")
#    print(respond(user_input))

#def respond(text):
#    text = text.lower()
#    if "hello" in text or "hi" in text:
#        return "Hello there!"
#    elif "bye" in text:
#        return "Goodbye!"
#    elif "how are you" in text:
#        return "I am fine"
#    elif "thanks" in text:
#        return "You're welcome"
#    elif "help" in text:
#        return "How can I assist?"
#    else:
#        return "I don't understand"
    
#if __name__ == "__main__":
#    main()

#Case normalization
#text = input("Write something: ").upper()
#if "hello" in text:
#    print("Hello there")

#if "HELLO" in text:
#    print("HELLO THERE")


#Day 5 Patterns and smarter logic
#So far we have been asking, is this word in text? Now we ask, how many? what type? what pattern?
#Part 1: Using lists for pattern detection
#Instead of writing if "hey" in text or if "hello" in text: we use a list to group patterns

#text = input("Say something: ").lower()
#greetings = ["hello", "hi", "hey", "waddupp"]
#for word in greetings:
#    if word in text:
#        print("Greetings detected")
#        break #this is a control flow mechanism. Think "stop searching once you find it"

#Part 3: Detecting numbers using .isdigit() -returns True if character is a number.
#text = "abc123"
#for char in text:
#    if char.isdigit():
#        print("Number found")
#        break

#Part 4: Counting patterns -we don't just detect, we measure.
#text = "abc12345xyz"
#count = 0

#for char in text:
#    if char.isdigit():
#        count += 1
#print(count)

#Part 5: Flags - Sometimes we need to track, did we find x? did we find y? An example of a flag is: has_letter = False. A flag that
#changes when a condition is met.

#text = input("Enter password: ")
#has_letter = False #flag
#has_number = False #flag

#for char in text:
#    if char.isalpha(): #.isalpha return True if all characters in the str are alphabetic and there is atleast 1 character, False otherwise
#        has_letter = True
#    if char.isdigit(): #.isdigit return True if all characters in the str are digits and there is at least on character, False otherwise
#        has_number = True

#if has_letter and has_number: #combining conditions for multiple checks. Only True if both are True
#    print("Strong Password")
#else:
#    print("Weak Password")

#This works because you scan the text, update the flags and decide at the end.

#Day 5 practice
#text = input("Say something: ").lower()
#greetings = ["hi", "hello", "hola"]
#for word in greetings:
#    if word in text:
#        print("Greetings Detected")
#        break #stop checking once you find a match.

#text = "abc12345xyz"
#count = 0
#for char in text:
#    if char.isdigit():
#        count += 1
#print(count)

#text = "hello123!!!"
#count = 0
#for char in text:
#    if char.isalpha():
#        count += 1
#print(count)

#text = input("Password: ")
#has_number = False #set flag
#has_letter = False #set flag

#Loop through text and find patterns or numbers and letters
#for char in text:
#    if char.isalpha():
#        has_letter = True
#    if char.isdigit():
#        has_number = True

#Set conditions. If password has a number and a letter at least or not.
#if has_letter and has_number:
#    print("Strong Password")
#else:
#    print("Weak Password")
#We can also finish this code with:
#if has_letter and has_number:
    #break #this stops the loop early and is more efficient.As per the question, if a digit and a letter have been detected stop the loop.


#def main():
#    user_input = input("Write something: ")
#    analyze(user_input)

#def analyze(text):
#    letters = 0
#    numbers = 0
#    others = 0

#    for char in text:
#        if char.isalpha():
#            letters += 1
#        elif char.isdigit():
#            numbers += 1
#        else:
#            others += 1

#    print(f"Letters: {letters}")
#    print(f"Numbers: {numbers}")
#    print(f"Others: {others}")

#if __name__ == "__main__":
#    main()

#Day 6: Real Problems (Combining everything: loops + conditions + strings + lists + logic)
#Problem 1: Name formatter

#text = ("   jOhN    doE   ").strip().lower()
#separated_text = (text).split()
#clean_text =" ".join(separated_text)
#final_text = clean_text.title()
#print(final_text)

#The above code can be compressed to just a few lines of code like this. Chaining the Pythonic way
#text = "   jOhN     doE    "
#final_text = " ".join(text.strip().lower().split()).title()
#print(final_text)


#Problem 2: Email Normalizer

#email = ("   JohnDoe@GMAIL.com   ").strip().lower()
#print(email)

#Problem 3: Word Counter
#text = ("Hello hello HELLO").lower()
#count = 0
#separated_text = text.split()
#for word in separated_text:
#    if word == "hello":
#        count += 1
#print(f"hello: {count}")

#Problem 4: Password Validator (Advanced)
#password = input("Password: ")

#Flags
#has_letter = False
#has_number = False

#Loop through the password to check for at least 1 number and at least 1 letter then break out of the loop
#for char in password:
#    if char.isalpha():
#        has_letter = True
#    if char.isdigit():
#        has_number = True

#Logic/ Conditions
#if len(password) >= 8 and has_letter and has_number:
#    print("Valid")
#else: print("Invalid")

#Problem 5: Clean and Analyze
#def main():
#    text = "   Hello!!! 123 WORLD!!!   "

    #Fucntion calls to clean and analyze text
#    clean = cleaned_text(text)
#    letters, numbers = analyze_text(text)

    #Print output of cleaning and analyzing text
#    print(clean)
#    print(f"Letters: {letters}")
#    print(f"Numbers: {numbers}")

#Define cleaned_text and analyze_text functions
#def cleaned_text(t):
#    t = t.strip().lower()
#    clean_text = t.replace("!", "").replace("123", "")
#    words = clean_text.split()
#    return " ".join(words)

#def analyze_text(text):
#    letters = 0
#    numbers = 0

#    for char in text:
#        if char.isalpha():
#            letters += 1

#        elif char.isdigit():
#            numbers += 1
    
#    return letters, numbers

#if __name__ == "__main__":
#    main()

#Day 7: Building new data from pieces using lists and append()- add an item to the end of the list. We use append when we dont know
#in advance how many items we'll have
#Part 1
#Create empty list
#words = []
#Add items to the list using append
#words.append("Hello")
#words.append("World")
#print(words)

#The camelCase problem. e.g. helloWorldPythonCode. Rules: First word-lowercase, Every next word- first letter uppercase, No spaces
text = "hello world python code"
#Break the text into pieces
words = text.split()

#Create a list to store the pieces
new_words = []

#Modify pieces
for i, word in enumerate(words):
    if i == 0:
        new_words.append(word.lower())
    else:
        new_words.append(word.capitalize())

#Join and print
camel = "".join(new_words)
print(camel)