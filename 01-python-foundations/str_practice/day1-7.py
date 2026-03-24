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
text = "I love Python"
separated = text.split()
combined = "...".join(separated)
print (separated)
print(combined)

#Fix messy spaces
new_text = "hello    world    again"
new_separated = new_text.split()
clean_text = " ".join(new_separated)
print(clean_text)

#Count words
words = "I love data science"
new_words = words.split()
count = 0
for char in new_words:
    if char != " ":
        count += 1
print(count)

#Reverse word order
motto = "I love Python"
new_motto = motto.split()
new_motto.reverse() #use reverse to reverse a list. Turn a str to a list then reverse it.
clean_motto = " ".join(new_motto)
print(clean_motto)
