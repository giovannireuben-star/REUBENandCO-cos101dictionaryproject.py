import streamlit as st

# 1. Database: Each group member can manage one of these dictionaries
translations = {
    "Igbo": {
        "Hello": "Ndewo", "Water": "Mmiri", "Food": "Nri", "House": "Ulo", "God": "Chukwu"
    },
    "Hausa": {
        "Hello": "Sannu", "Water": "Ruwa", "Food": "Abinci", "House": "Gida", "God": "Allah"
    },
    "Yoruba": {
        "Hello": "Bawo", "Water": "Omi", "Food": "Ounjẹ", "House": "Ile", "God": "Olorun"
    },
    "Idoma": {
        "Hello": "Aba", "Water": "Eyi", "Food": "Oje", "House": "Ola", "God": "Owoicho"
    },
    "Igala": {
        "Hello": "Aba", "Water": "Omi", "Food": "Jeun", "House": "Unyi", "God": "Ojo"
    }
}

# 2. Interface Header
st.set_page_config(page_title="G-Squad Dictionary", page_icon="📖")
st.title("📖 G-Squad Multi-Language Dictionary")
st.markdown("---")

# 3. The Search Bar
word = st.text_input("Search Bar", placeholder="Type an English word (e.g., Water)...").strip().title()

st.write("### Select Language to Translate:")

# 4. Creating Buttons for each Language
# We create 5 columns for the 5 languages
cols = st.columns(5)
languages = list(translations.keys())

for i, col in enumerate(cols):
    lang_name = languages[i]
    with col:
        if st.button(lang_name):
            if word == "":
                st.warning("Enter a word!")
            elif word in translations[lang_name]:
                result = translations[lang_name][word]
                st.success(f"**{lang_name}:**\n\n# {result}")
            else:
                st.error(f"'{word}' not found in {lang_name}.")

# 5. Information Section
st.markdown("---")
st.info("💡 **Instructions:** Type your word in English first, then click the language button to see the translation.")