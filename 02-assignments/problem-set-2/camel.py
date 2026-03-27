text = input("camelCase: ")
words = text.split()

new_words = []

for i, word in enumerate(words):
    if i == 0:
        new_words.append(word.lower())
    else:
        new_words.append(word.capitalize())

camel = "".join(new_words)
print(camel)
