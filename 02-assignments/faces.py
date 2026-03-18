def main():
    #Get user input
    user_input = input("How do you feel today? ")
    user_input = convert(user_input)
    print(user_input)

def convert(text):
    text = text.replace(":)","😊")
    text = text.replace(":(","☹️")
    return text

main()

