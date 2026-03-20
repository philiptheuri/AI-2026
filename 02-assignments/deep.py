#Ask the question
qn = " ".join(input("What is the Answer to the Great Question of Life, the Universe and Everything? ").lower().split())

#Create and print the logic
if qn == "42":
    print("Yes")

elif qn == "forty two":
    print("Yes")

elif qn == "forty-two":
    print("Yes")

else:
    print("No")
