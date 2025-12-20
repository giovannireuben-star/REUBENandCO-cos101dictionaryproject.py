hausa_dictionary = {
    "Hello": "Sannu",
    "Thank you": "Na gode",
    "Water": "Ruwa",
    "Food": "Abinci",
    "Mother": "Uwa",
    "Father": "Uba",
    "House": "Gida",
    "Book": "Littafi",
    "School": "Makaranta",
    "Child": "Yaro",
    "Man": "Namiji",
    "Woman": "Mace",
    "Sun": "Rana",
    "Moon": "Wata",
    "Star": "Tauraro",
    "Love": "Soyayya",
    "God": "Allah",
    "Friend": "Aboki",
    "Name": "Suna",
    "Market": "Kasuwa"
}

while True:
    word = input("Enter an English word to translate to Hausa (or type 'exit' to quit): ").strip()

    if word == "":
        print("Please enter an English word to translate.")
        continue

    if word.lower() == "exit":
        print("Goodbye!")
        break

    if word.islower():
        word = word.title()

    translation = hausa_dictionary.get(word)

    if translation:
        print(f"The Hausa translation of '{word}' is '{translation}'.")
    else:
        print("Word not found in the dictionary.")
