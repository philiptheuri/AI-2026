#This program removes vowels from user input
text = input("Say something: ").lower()
result = " "
for t in text:
    if t not in "aeiou":
        result += t
print(result)