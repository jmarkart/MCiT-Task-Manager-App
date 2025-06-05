import streamlit as st
from search_utils import search_tasks
from task_utils import get_all_categories, get_filtered_tasks, update_task_status
from category_utils import get_category_filter
from status_utils import STATUS_OPTIONS

st.title("🔍 Aufgaben durchsuchen und Status ändern")

# Session State initialisieren
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

# Kategorie-Filter
all_categories = get_all_categories()
selected_category = get_category_filter(all_categories)

# Suchfeld
search_query = st.text_input("Suchbegriff eingeben")

# Vorfiltern nach Kategorie
if selected_category == "Alle Kategorien":
    filtered_tasks = st.session_state["tasks"]
else:
    filtered_tasks = get_filtered_tasks(selected_category)

# Suchen
results = search_tasks(filtered_tasks, search_query)

st.subheader("Suchergebnisse")
if results:
    for idx, task in enumerate(results):
        status = st.selectbox(
            f"Status für '{task['Betreff']}' ändern",
            STATUS_OPTIONS,
            index=STATUS_OPTIONS.index(task["Status"]),
            key=f"search_status_{task['Betreff']}_{task['Fällig']}",
        )
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
    st.info("Keine Aufgaben gefunden.")
