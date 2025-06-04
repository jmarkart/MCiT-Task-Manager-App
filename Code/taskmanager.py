import streamlit as st

st.set_page_config(
    page_icon="💥",
    page_title="Jonis Task Managers",
    layout="centered"
)

st.title("Joni's Task Manager")

st.markdown(
    "Herzlich willkommen in meiner **Task Manager App**. Hier können Tasks verwaltet werden, um sich selbst noch besser zu organisieren. **Hol das beste aus dir raus! 💯🔅✔**."
)

# Kategorie-Vorschläge
category_options = ["Uni", "Arbeit", "Privat", "Haushalt", "Sonstiges", "Andere"]

# Eingabefelder
due_date = st.date_input("Fälligkeitsdatum wählen")
reminder_date = st.date_input("Erinnerungsdatum wählen")
subject = st.text_input("Aufgabenbetreff eingeben")
description = st.text_area("Beschreibung einfügen")
priority = st.selectbox("Priorität wählen", ["Hoch", "Mittel", "Niedrig"])

category_selection = st.selectbox("Kategorie wählen", category_options)
if category_selection == "Andere":
    category = st.text_input("Eigene Kategorie eingeben")
else:
    category = category_selection

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
        "Kategorie": category,
        "Erledigt": done,
        "Status": "Abgeschlossen" if done else "Offen",
    })
    st.success("Task hinzugefügt!")

# Kategorien für Filter-Selectbox aufbereiten
all_categories = list({task["Kategorie"] for task in st.session_state["tasks"] if task["Kategorie"]})
for vorschlag in category_options:
    if vorschlag != "Andere" and vorschlag not in all_categories:
        all_categories.append(vorschlag)
all_categories = sorted(set(all_categories))
all_categories.insert(0, "Alle Kategorien")

selected_category = st.selectbox(
    "Nach Kategorie filtern",
    all_categories,
    key="category_filter"
)

# Tasks filtern
if selected_category == "Alle Kategorien":
    filtered_tasks = st.session_state["tasks"]
else:
    filtered_tasks = [task for task in st.session_state["tasks"] if task["Kategorie"] == selected_category]

st.subheader("Deine Aufgaben")
if filtered_tasks:
    for i, task in enumerate(filtered_tasks, 1):
        st.write(
            f"{i}. **[{task['Kategorie']}]** {task['Betreff']} "
            f"(Priorität: {task['Priorität']}, Fällig: {task['Fällig']}, "
            f"Erledigt: {'✅' if task['Erledigt'] else '❌'})"
        )
else:
    st.info("Keine Aufgaben gefunden.")

# Aktive Aufgaben (nicht abgeschlossen)
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
            f"{icon} **[{task['Kategorie']}] {task['Betreff']}** (Priorität: {task['Priorität']}, Fällig: {task['Fällig']})"
        )

# Abgeschlossene Aufgaben
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
                f"{icon} ~~[{task['Kategorie']}] {task['Betreff']}~~ (Priorität: {task['Priorität']}, Fällig: {task['Fällig']})"
            )
