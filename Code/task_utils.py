import streamlit as st

def get_filtered_tasks(selected_category):
    # Alle Aufgaben, wenn "Alle Kategorien" gewählt ist
    if selected_category == "Alle Kategorien":
        return st.session_state["tasks"]
    # Gefilterte Aufgaben nach Kategorie
    return [task for task in st.session_state["tasks"] if task.get("Kategorie") == selected_category]

def get_all_categories():
    # Gibt alle Kategorien zurück, die im tasks-Array verwendet werden
    categories = list({task.get("Kategorie") for task in st.session_state["tasks"] if task.get("Kategorie")})
    categories.sort()
    return categories

def update_task_status(index, new_status):
    st.session_state["tasks"][index]["Status"] = new_status
    st.session_state["tasks"][index]["Erledigt"] = (new_status == "Abgeschlossen")

def add_task(
    due_date, reminder_date, subject, description, priority, category, done,
    note, file, link
):
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
        "Notiz": note,
        "Anhang": file,
        "Link": link
    })
