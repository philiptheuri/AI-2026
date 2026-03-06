#Ask for the name
#name=input("What is your name? ").strip().title()

#Split function, split first name and last name.
#first, last = name.split(" ")
#print(f"Hello, {first}")

#Ask for the age
#age=int (input("How old are you? "))

#Ask where user lives
#country=input("Where do you live? ").strip().title()

#Display the answers and the different string/output features

#Printing Hello and the inputted name using + (concatenation)
#print("Hello," + name)

#Using a comma to pass in multiple arguments. In this case passing text plus the variable "age". You
#can use commas to pass multiple arguments.
#print("You are",age,"years old")

"""The print function automatically includes the end='\n'. This \n indicates that the print function 
 will automatically create a line break when run. The function takes an argument called end, and the
 default is to create a new line. However, we can technically provide an argument for end ourselves
 such that a new line is not created.
"""

#This output also includes the use of quotation marks on the word "sucks"
#print(f"Oh really! You live in ",end="")
#print(f"{country}? That \"sucks\"!")

#Using the special f indicator to ask python to treat this string in a special way (str formatting)
#Using the strip method to remove any white space from the string
#president = input(f"Who was the 3rd president of {country}?").strip().title()
#print(f"Was {president} a good leader for {country}?")
#answer = str(input("")).capitalize().strip()

#Using the title method to title case a name
#Remove whitespace from str
#Capitalize the first letter of each word
#place = input(f"What is your favourite place in {country}?").strip().title()


#Print the output using the special f indicator
#print(f"Great choice, {place}")

#You can combine strip() and title() into one line of code
#bar = input("What is you favourite bar? ").strip().title()
#print(f"Ah! So you like {bar} too?")
