import streamlit as st
from task_utils import get_filtered_tasks, get_all_categories, update_task_status
from category_utils import get_category_filter
from status_utils import STATUS_OPTIONS

# --- Session-State initialisieren ---
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

from task_utils import get_filtered_tasks, get_all_categories, update_task_status
from category_utils import get_category_filter
from status_utils import STATUS_OPTIONS

st.title("Aufgabenliste")

# Kategorien-Filter
all_categories = get_all_categories()
selected_category = get_category_filter(all_categories)

# Status-Filter
status_options = ["Alle", "Offen", "In Bearbeitung", "Abgeschlossen"]
selected_status = st.selectbox("Status filtern", status_options)

tasks = get_filtered_tasks(selected_category)

if selected_status != "Alle":
    tasks = [t for t in tasks if t["Status"] == selected_status]

# Sortieroptionen
sort_option = st.selectbox(
    "Sortieren nach",
    [
        "Fälligkeitsdatum aufsteigend",
        "Fälligkeitsdatum absteigend",
        "Priorität (Hoch → Niedrig)",
        "Priorität (Niedrig → Hoch)",
    ],
)

def prio_value(priority):
    mapping = {"Hoch": 2, "Mittel": 1, "Niedrig": 0}
    return mapping.get(priority, -1)

if sort_option == "Fälligkeitsdatum aufsteigend":
    tasks = sorted(tasks, key=lambda t: t["Fällig"])
elif sort_option == "Fälligkeitsdatum absteigend":
    tasks = sorted(tasks, key=lambda t: t["Fällig"], reverse=True)
elif sort_option == "Priorität (Hoch → Niedrig)":
    tasks = sorted(tasks, key=lambda t: prio_value(t["Priorität"]), reverse=True)
elif sort_option == "Priorität (Niedrig → Hoch)":
    tasks = sorted(tasks, key=lambda t: prio_value(t["Priorität"]))

st.subheader("Übersicht")
if tasks:
    for idx, task in enumerate(tasks):
        # Status ändern (achtet auf den Index im Haupt-task-Array!)
        status = st.selectbox(
            f"Status für '{task['Betreff']}' ändern",
            STATUS_OPTIONS,
            index=STATUS_OPTIONS.index(task["Status"]),
            key=f"status_{task['Betreff']}_{task['Fällig']}",
        )
        # Update im Original-Array suchen und ändern
        for i, orig_task in enumerate(st.session_state["tasks"]):
            if (
                orig_task["Betreff"] == task["Betreff"]
                and orig_task["Fällig"] == task["Fällig"]
                and orig_task["Beschreibung"] == task["Beschreibung"]
            ):
                update_task_status(i, status)
                break

        st.markdown(
            f"**{idx+1}. [{task['Kategorie']}] {task['Betreff']}**  \n"
            f"- **Fällig:** {task['Fällig']}  \n"
            f"- **Priorität:** {task['Priorität']}  \n"
            f"- **Status:** {status}  \n"
            f"- **Beschreibung:** {task['Beschreibung']}"
        )
        st.write("---")
else:
    st.info("Keine Aufgaben vorhanden.")
