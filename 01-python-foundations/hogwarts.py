#Creating a list
#students = ["Hermoine","Harry","Ron"]

#How to print the list manually, one item at a time.
#print(students[0])
#print(students[1])
#print(students[2])

#A better way to do it using a for loop. Notice that we didn't use the _ in the for loop because this time we are using the variable and
#to use an underscore in this way will make your code confusing. You also don't need to initialize the student variable, Python takes
#care of that.

#for student in students:
#    print(student)

#len function. We can use len as a way of checking the length of the list called students. Remember, range doesn't take a list of 
#strings, it takes a number and for this example, the number is 3 so I get a range of values 0,1 and 2. So we first get the length of 
#the students list, that is going to be 3 then we pass that return value as the argument to range, that's going to give me back a range
#of values 0, then 1, then 2. We can print multiple things at a time so we are printing not just the students at location i but rather i
#first and the student at location i. We add a + 1 to the i so that it can show the user that Hermoine is the top ranked student, 1,
#followed by Harry at 2 and Ron at 3. Remember, Python starts counting at 0.

#students = ["Hermoine","Harry","Ron"]

#for i in range(len(students)):
#    print(i + 1, students[i])

#dict
#dicts or dictionaries are a data structure that allows you to associate keys with values. Where a list is a list of multiple values,
# a dict associates a key with a value.
#Considering the houses of Hogwarts, we might assign specific students to specific houses. We could use lists alone to accomplish this.

#students = ["Hermoine","Harry","Ron","Draco"]
#houses = ["Griffyndor", "Griffyndor","Griffyndor","Slytherin"]

#The individual at the first position of students is associated with the house at the first position of the houses list and so on.
#However, this can be quite cumbersome as the list grows! We can better our code using a dict as follows:

#students = {
#    "Hermoine": "Griffyndor",
#    "Harry": "Griffyndor",
#    "Ron": "Griffyndor",
#    "Draco": "Slytherin",
#}
#print(students["Hermoine"])
#print(students["Harry"])
#print(students["Ron"])
#print(students["Draco"])

#We use curly braces when creating a dict. Where lists use numbers to iterate through the list, dicts allow us to use words. In this
#example, "Hermoine" is the key and "Griffyndor" is the value.
#We can improve our code as follows:

#students = {
#    "Hermoine": "Griffyndor",
#    "Harry": "Griffyndor",
#    "Ron": "Griffyndor",
#    "Draco": "Slytherin",
#}
#for student in students:
#    print(student)

#Executing this code, the for loop will only iterate through all the keys, resulting in a list of the names of the students. When
# you use a for loop in Python to iterate over a dictionary, by design, it iterates over all of the keys.
#How could we print out both values and keys? We modify our code as follows:

#students = {
#    "Hermoine": "Griffyndor",
#    "Harry": "Griffyndor",
#    "Ron": "Griffyndor",
#    "Draco": "Slytherin",
#}
#for student in students:
#    print(student, students[student])

#Notice how students[student] will go to each students key and find the value of their house. If the students name is the key, then
#this syntax, students[student] will go to Hermoines location and get back her house
#The output is a bit messy and we can addthe separator argument, sep = ",", to the print function to create a clean separation
#of a , between each item printed.

#students = {
#    "Hermoine": "Griffyndor",
#    "Harry": "Griffyndor",
#    "Ron": "Griffyndor",
#    "Draco": "Slytherin",
#}

#for student in students:
#    print(student, students[student], sep=",")

#What if we have more information about our students? How could we associate more data with the students?
#Imagine wanting to have lots of data associated with multiple keys. The keys in this example are name, house and patronus and the values
#or definitions are the data associated with the keys e.g. Hermoine, Griffyndor and Otter.

students = [
    {"name": "Hermoine", "house": "Griffyndor", "patronus": "Otter"},
    {"name": "Harry", "house": "Griffyndor", "patronus": "Stag"},
    {"name": "Ron", "house": "Griffyndor", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]
#Notice how this code creates a list of four dicts. The list called students has four dicts each associated with one student. Also,
#Python has a special None designation where there is no value associated with a key.
#Now we have access to a whole host of interesting data about these students and we can add the following code.

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

#Notice how the for loop will iterate through each of the dicts inside the list called students.