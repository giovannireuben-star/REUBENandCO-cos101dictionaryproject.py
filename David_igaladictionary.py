igala_dictionary = {
    "Hello": "Aneje",
    "Thank you": "Ameyo",
    "Water": "Ama",
    "Food": "Uje",
    "Mother": "Nne",
    "Father": "Apa",
    "House": "Uno",
    "Book": "Ekpulu",
    "School": "Uno ekpulu",
    "Child": "Omo",
    "Man": "Onuwo",
    "Woman": "Onubi",
    "Sun": "Ogene",
    "Moon": "Ogida",
    "Star": "Ukwu",
    "Love": "Ifunanya",
    "God": "Ojo",
    "Friend": "Oyi",
    "Name": "Izina",
    "Market": "Uloja"
}

while True:
    word = input("Enter an English word to translate to Igala (or type 'exit' to quit): ").strip()

    if word == "":
        print("Please enter an English word to translate.")
        continue

    if word.lower() == "exit":
        print("Goodbye!")
        break

    if word.islower():
        word = word.title()

    translation = igala_dictionary.get(word)

    if translation:
        print(f"The Igala translation of '{word}' is '{translation}'.")
    else:
        print("Word not found in the dictionary.")