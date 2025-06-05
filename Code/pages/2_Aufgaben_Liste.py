import streamlit as st
from task_utils import get_filtered_tasks, get_all_categories, update_task_status
from category_utils import get_category_filter
from status_utils import STATUS_OPTIONS

st.title("Aufgabenliste")

# Filter
all_categories = get_all_categories()
selected_category = get_category_filter(all_categories)

# Optional: Nach Status filtern
status_options = ["Alle", "Offen", "In Bearbeitung", "Abgeschlossen"]
selected_status = st.selectbox("Status filtern", status_options)

tasks = get_filtered_tasks(selected_category)

if selected_status != "Alle":
    tasks = [t for t in tasks if t["Status"] == selected_status]

# Nach Fälligkeitsdatum sortieren (optional)
tasks = sorted(tasks, key=lambda t: t["Fällig"])

st.subheader("Übersicht")
if tasks:
    for i, task in enumerate(tasks, 1):
        status = st.selectbox(
            f"Status für '{task['Betreff']}' ändern",
            STATUS_OPTIONS,
            index=STATUS_OPTIONS.index(task["Status"]),
            key=f"status_{i}",
        )
        update_task_status(i-1, status)  # i-1, weil enumerate bei 1 startet, Liste aber bei 0
        st.markdown(
            f"**{i}. [{task['Kategorie']}] {task['Betreff']}**  \n"
            f"- **Fällig:** {task['Fällig']}  \n"
            f"- **Priorität:** {task['Priorität']}  \n"
            f"- **Status:** {status}  \n"
            f"- **Beschreibung:** {task['Beschreibung']}"
        )
        st.write("---")
else:
    st.info("Keine Aufgaben vorhanden.")
