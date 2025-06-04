import streamlit as st

CATEGORY_OPTIONS = ["Uni", "Arbeit", "Privat", "Haushalt", "Sonstiges", "Andere"]

def get_category_input():
    category_selection = st.selectbox("Kategorie wählen", CATEGORY_OPTIONS)
    if category_selection == "Andere":
        return st.text_input("Eigene Kategorie eingeben")
    return category_selection

def get_category_filter(all_categories):
    all_cats = list(sorted(set(all_categories)))
    all_cats.insert(0, "Alle Kategorien")
    return st.selectbox("Nach Kategorie filtern", all_cats, key="category_filter")
