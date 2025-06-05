import streamlit as st
from search_utils import search_tasks
from task_utils import get_all_categories, get_filtered_tasks

st.title("Aufgaben und Kategorien durchsuchen")

# Kategorie-Filter
all_categories = get_all_categories()
selected_category = st.selectbox("Nach Kategorie filtern", ["Alle Kategorien"] + all_categories, key="search_category")

search_query = st.text_input("Suchbegriff eingeben")

if selected_category == "Alle Kategorien":
    filtered_tasks = st.session_state.get("tasks", [])
else:
    filtered_tasks = get_filtered_tasks(selected_category)

results = search_tasks(filtered_tasks, search_query)

st.subheader("Suchergebnisse")
if results:
    for i, task in enumerate(results, 1):
        st.write(
            f"{i}. **[{task['Kategorie']}]** {task['Betreff']} "
            f"(Priorität: {task['Priorität']}, Fällig: {task['Fällig']}, "
            f"Status: {task['Status']})"
        )
else:
    st.info("Keine Aufgaben gefunden.")
