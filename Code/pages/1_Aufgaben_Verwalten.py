import streamlit as st
from task_utils import add_task
from category_utils import get_category_input

st.title("Aufgaben verwalten")

due_date = st.date_input("Fälligkeitsdatum wählen")
reminder_date = st.date_input("Erinnerungsdatum wählen")
subject = st.text_input("Aufgabenbetreff eingeben")
description = st.text_area("Beschreibung einfügen")
priority = st.selectbox("Priorität wählen", ["Hoch", "Mittel", "Niedrig"])
category = get_category_input()
done = st.checkbox("Erledigt")

if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

if st.button("Task hinzufügen"):
    add_task(due_date, reminder_date, subject, description, priority, category, done)
    st.success("Task hinzugefügt!")
