def add_task(due_date, reminder_date, subject, description, priority, category, done):
    import streamlit as st
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

def get_all_categories():
    import streamlit as st
    categories = list({task["Kategorie"] for task in st.session_state["tasks"] if task["Kategorie"]})
    return sorted(set(categories + ["Uni", "Arbeit", "Privat", "Haushalt", "Sonstiges"]))

def get_filtered_tasks(selected_category):
    import streamlit as st
    if selected_category == "Alle Kategorien":
        return st.session_state["tasks"]
    return [task for task in st.session_state["tasks"] if task["Kategorie"] == selected_category]

def update_task_status(task_index, new_status):
    import streamlit as st
    st.session_state["tasks"][task_index]["Status"] = new_status
