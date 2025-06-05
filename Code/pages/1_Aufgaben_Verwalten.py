import streamlit as st
import datetime
from task_utils import add_task

st.title("Aufgaben verwalten")

CATEGORY_OPTIONS = ["Uni", "Arbeit", "Privat", "Haushalt", "Sonstiges", "Andere"]
today = datetime.date.today()

# 1. Trigger: Soll nach Button alles zurückgesetzt werden?
if "reset_fields" not in st.session_state:
    st.session_state["reset_fields"] = False

if st.session_state.reset_fields:
    # Nur dann Felder zurücksetzen, wenn das Trigger-Flag gesetzt ist (und VOR den Widgets!)
    st.session_state["due_date"] = today
    st.session_state["reminder_date"] = today
    st.session_state["subject"] = ""
    st.session_state["description"] = ""
    st.session_state["priority"] = "Mittel"
    st.session_state["category_select"] = CATEGORY_OPTIONS[0]
    st.session_state["category_custom"] = ""
    st.session_state["done"] = False
    st.session_state.reset_fields = False  # Trigger wieder löschen

# Felder initialisieren, wenn sie nicht existieren
if "due_date" not in st.session_state:
    st.session_state["due_date"] = today
if "reminder_date" not in st.session_state:
    st.session_state["reminder_date"] = today
if "subject" not in st.session_state:
    st.session_state["subject"] = ""
if "description" not in st.session_state:
    st.session_state["description"] = ""
if "priority" not in st.session_state:
    st.session_state["priority"] = "Mittel"
if "category_select" not in st.session_state:
    st.session_state["category_select"] = CATEGORY_OPTIONS[0]
if "category_custom" not in st.session_state:
    st.session_state["category_custom"] = ""
if "done" not in st.session_state:
    st.session_state["done"] = False

# Jetzt werden die Widgets gebaut
due_date = st.date_input("Fälligkeitsdatum wählen", key="due_date")
reminder_date = st.date_input("Erinnerungsdatum wählen", key="reminder_date")
subject = st.text_input("Aufgabenbetreff eingeben", key="subject")
description = st.text_area("Beschreibung einfügen", key="description")
priority = st.selectbox("Priorität wählen", ["Hoch", "Mittel", "Niedrig"], key="priority")
category_select = st.selectbox("Kategorie wählen", CATEGORY_OPTIONS, key="category_select")
if category_select == "Andere":
    category = st.text_input("Eigene Kategorie eingeben", key="category_custom")
else:
    category = category_select
done = st.checkbox("Erledigt", key="done")

if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

if st.button("Task hinzufügen"):
    add_task(due_date, reminder_date, subject, description, priority, category, done)
    st.success("Task hinzugefügt!")

    # Nur das Flag setzen, die eigentliche Rücksetzung passiert im nächsten Render-Durchlauf
    st.session_state.reset_fields = True
    st.rerun()
