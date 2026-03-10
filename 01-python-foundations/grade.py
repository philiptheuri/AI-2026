#and statement. Similar to or statement, and can be used within conditional statements.

#score = int(input("Score: "))

#if score >= 90 and score <= 100:
#    print("Grade: A")

#elif score >= 80 and score <= 90:
#    print("Grade: B")

#elif score >= 70 and score <= 80:
#    print("Grade: C")

#elif score >= 60 and score <= 70:
#    print("Grade: D")

#else:
#    print("Grade: F")

#This code has the potential for bugs. For example does scoring 90 give you an A grade or a B grade?
#Secondly, we don't want to trust our users to input their own information. (Find out what the problem
#with this is exactly from the lecturers explanation). Another error is that if the user puts a number
#like 110, it brings a grade F.
#We could improve our code as follows:

#score = int(input("Score: "))

#if 90 <= score <= 100:
#    print("Grade: A")

#elif 80 <= score < 90:
#    print("Grade: B")

#elif 70 <= score < 80:
#    print("Grade: C")

#elif 60 <= score < 70:
#    print("Grade: D")

#else:
#    print("Grade: F")

#Still, we can further improve the program by asking fewer questions.

score = int(input("Score: "))

if score >= 90:
    print("Grade: A")

elif score >= 80:
    print("Grade: B")

elif score >= 70:
    print("Grade: C")

elif score >= 60:
    print("Grade: D")

else:
    print("Grade: F")
