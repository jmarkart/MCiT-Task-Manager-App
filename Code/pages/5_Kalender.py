import streamlit as st
from streamlit_calendar import calendar
from datetime import datetime

st.title("📅 Kalenderansicht")

# Session State initialisieren
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

# Events aus Aufgaben bauen
events = []
for idx, task in enumerate(st.session_state["tasks"]):
    # Nur wenn ein Fälligkeitsdatum vorhanden
    if task.get("Fällig"):
        events.append({
            "id": str(idx),
            "title": task["Betreff"],
            "start": str(task["Fällig"]),
            "end": str(task["Fällig"]),
            "extendedProps": {
                "Priorität": task.get("Priorität"),
                "Kategorie": task.get("Kategorie"),
                "Beschreibung": task.get("Beschreibung"),
                "Notiz": task.get("Notiz"),
                "Status": task.get("Status"),
            },
        })

calendar_options = {
    "initialView": "dayGridMonth",
    "locale": "de",
    "headerToolbar": {
        "left": "prev,next today",
        "center": "title",
        "right": "dayGridMonth,timeGridWeek,timeGridDay"
    },
    "eventClick": True,  # Damit wir auf Events klicken können
}

clicked_event = calendar(events, options=calendar_options, key="calendar")

# Popup für Event-Details
if clicked_event and "event" in clicked_event:
    e = clicked_event["event"]
    st.markdown("### 📋 Termin-Details")
    st.info(f"**{e['title']}**<br>"
            f"**Datum:** {e['start']}<br>"
            f"**Priorität:** {e['extendedProps'].get('Priorität','') }<br>"
            f"**Status:** {e['extendedProps'].get('Status','')}<br>"
            f"**Kategorie:** {e['extendedProps'].get('Kategorie','')}<br>"
            f"**Beschreibung:** {e['extendedProps'].get('Beschreibung','') }<br>"
            f"**Notiz:** {e['extendedProps'].get('Notiz','') }",
            unsafe_allow_html=True)

