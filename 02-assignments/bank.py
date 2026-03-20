#Prompts the user for greeting. Ignore any leading whitespace in the user's greetings and treat the user's greeting case insensitively
prompt = " ".join(input("Greeting: ").lower().split())

#Conditionals and logic
if (prompt).startswith("hello"):
    print("$0")

elif(prompt).startswith("h") and prompt != "hello":
    print("$20")

else:
    print("$100")