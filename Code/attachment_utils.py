import streamlit as st

def attachment_inputs():
    note = st.text_area("Notiz zur Aufgabe (optional)", key="note")
    file = st.file_uploader("Anhang (z. B. PDF)", type=["pdf"])
    link = st.text_input("Externer Link (optional)", key="attachment_link")
    return note, file, link
