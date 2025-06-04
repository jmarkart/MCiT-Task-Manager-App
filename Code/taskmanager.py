import streamlit as st

st.set_page_config(
    page_icon="💥",
    page_title="Jonis Task Managers",
    layout="centered"
)

st.title("Joni's Task Manager")

st.markdown("Herzlich willkommen in meiner **Task Manager App**. Hier können Tasks verwaltet werden, um sich selbst noch besser zu organisieren. **Hol das beste aus dir raus! 💯🔅✔**.")

# Eingabefelder
due_date = st.date_input("Fälligkeitsdatum wählen")
reminder_date = st.date_input("Erinnerungsdatum wählen")
subject = st.text_input("Aufgabenbetreff eingeben")
description = st.text_area("Beschreibung einfügen")
priority = st.selectbox("Priorität wählen", ["Hoch", "Mittel", "Niedrig"])
done = st.checkbox("Erledigt")

# Session State für Tasks
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

# Task hinzufügen
if st.button("Task hinzufügen"):
    st.session_state["tasks"].append({
        "Fällig": due_date,
        "Erinnerung": reminder_date,
        "Betreff": subject,
        "Beschreibung": description,
        "Priorität": priority,
        "Erledigt": done,
    })
    st.success("Task hinzugefügt!")

# Tasks anzeigen
st.subheader("Deine Aufgaben")
for i, task in enumerate(st.session_state["tasks"], 1):
    st.write(f"{i}. {task['Betreff']} (Priorität: {task['Priorität']}, Fällig: {task['Fällig']}, Erledigt: {'✅' if task['Erledigt'] else '❌'})")
