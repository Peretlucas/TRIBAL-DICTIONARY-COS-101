# Emarhe Gideon BHU/26/04/05/0107
# using key : value pairs
urhobo_dictionary = {
    "come": "rhee",
    "go": "kpo",
    "eat": "re",
    "stay": "dia",
    "water": "ame",
    "food": "emu",
    "clothes": "ewu",
    "sleep": "ovie",
    "jump": "kparhe",
    "dance": "gbe ughẹ",
    "play": "se ughẹ",
    "write": "kore",
    "read": "se ebe",
    "fool": "ogheghogho",
    "book": "ebe",
    "house": "ogwa",
    "mother": "oni",
    "father": "osa",
    "sister": "onem-oghele",
    "brother": "omote-oghele",
}

print(urhobo_dictionary)

word = input("Enter a word: ").lower()

if word not in urhobo_dictionary:
    print(f"sorry, we dont have {word} in the dictionary")
else:
    print(urhobo_dictionary[word])
