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
status_options = ["Offen", "In Bearbeitung", "Abgeschlossen"]
status_icons = {
    "Offen": "🔴",
    "In Bearbeitung": "🟡",
    "Abgeschlossen": "✅",
}

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
        "Status": "Abgeschlossen" if done else "Offen",
    })
    st.success("Task hinzugefügt!")

# Tasks anzeigen
st.subheader("Deine Aufgaben")
for i, task in enumerate(st.session_state["tasks"], 1):
    st.write(f"{i}. {task['Betreff']} (Priorität: {task['Priorität']}, Fällig: {task['Fällig']}, Erledigt: {'✅' if task['Erledigt'] else '❌'})")
st.subheader("Aktive Aufgaben")
for i, task in enumerate(st.session_state["tasks"]):
    if task["Status"] != "Abgeschlossen":
        status = st.selectbox(
            f"Status ändern für '{task['Betreff']}'",
            status_options,
            index=status_options.index(task["Status"]),
            key=f"status_{i}",
        )
        st.session_state["tasks"][i]["Status"] = status
        icon = status_icons[status]
        st.markdown(
            f"{icon} **{task['Betreff']}** (Priorität: {task['Priorität']}, Fällig: {task['Fällig']})"
        )

if any(t["Status"] == "Abgeschlossen" for t in st.session_state["tasks"]):
    st.subheader("Abgeschlossene Aufgaben")
    for i, task in enumerate(st.session_state["tasks"]):
        if task["Status"] == "Abgeschlossen":
            status = st.selectbox(
                f"Status ändern für '{task['Betreff']}'",
                status_options,
                index=status_options.index(task["Status"]),
                key=f"status_done_{i}",
            )
            st.session_state["tasks"][i]["Status"] = status
            icon = status_icons[status]
            st.markdown(
                f"{icon} ~~{task['Betreff']}~~ (Priorität: {task['Priorität']}, Fällig: {task['Fällig']})"
            )

            