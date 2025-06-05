import streamlit as st

st.set_page_config(
    page_title="Joni's Task Manager",
    page_icon="💥",
    layout="centered"
)

st.title("Willkommen zu Joni's Task Manager! 💥")

st.markdown(
    """
    Mit dieser Anwendung kannst du Aufgaben übersichtlich verwalten, nach Kategorien organisieren, suchen und den Status anpassen.

    Wähle im Menü links eine Seite, um loszulegen:
    - **Aufgaben verwalten:** Neue Aufgaben anlegen, filtern und Status ändern
    - **Suche:** Aufgaben nach Stichwort oder Kategorie durchsuchen
    - **Überblick:** (optional) Statistiken und Zusammenfassung

    **Hol das Beste aus dir raus! 💯🔅✔**
    """
)
