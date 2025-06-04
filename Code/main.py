import streamlit as st
from task_utils import add_task, get_filtered_tasks, get_all_categories, update_task_status
from category_utils import get_category_input, get_category_filter
from status_utils import STATUS_OPTIONS, STATUS_ICONS
from search_utils import search_tasks

st.set_page_config(
    page_icon="💥",
    page_title="Jonis Task Managers",
    layout="centered"
)

st.title("Joni's Task Manager")

st.markdown(
    "Herzlich willkommen in meiner **Task Manager App**. Hier können Tasks verwaltet werden, um sich selbst noch besser zu organisieren. **Hol das beste aus dir raus! 💯🔅✔**."
)

# Eingabefelder für neue Aufgabe
due_date = st.date_input("Fälligkeitsdatum wählen")
reminder_date = st.date_input("Erinnerungsdatum wählen")
subject = st.text_input("Aufgabenbetreff eingeben")
description = st.text_area("Beschreibung einfügen")
priority = st.selectbox("Priorität wählen", ["🦣", "🦙", "🦤"])
category = get_category_input()
done = st.checkbox("Erledigt")

if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

# Aufgabe hinzufügen
if st.button("Task hinzufügen"):
    add_task(due_date, reminder_date, subject, description, priority, category, done)
    st.success("Task hinzugefügt!")

# Kategorie-Filter
all_categories = get_all_categories()
selected_category = get_category_filter(all_categories)

# Suchfeld
search_query = st.text_input("Suche nach Aufgaben oder Kategorien")

# Tasks filtern (erst Kategorie, dann Suchbegriff)
filtered_tasks = get_filtered_tasks(selected_category)
filtered_tasks = search_tasks(filtered_tasks, search_query)

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
            STATUS_OPTIONS,
            index=STATUS_OPTIONS.index(task["Status"]),
            key=f"status_{i}",
        )
        update_task_status(i, status)
        icon = STATUS_ICONS[status]
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
                STATUS_OPTIONS,
                index=STATUS_OPTIONS.index(task["Status"]),
                key=f"status_done_{i}",
            )
            update_task_status(i, status)
            icon = STATUS_ICONS[status]
            st.markdown(
                f"{icon} ~~[{task['Kategorie']}] {task['Betreff']}~~ (Priorität: {task['Priorität']}, Fällig: {task['Fällig']})"
            )
