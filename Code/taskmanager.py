import streamlit as st

st.set_page_config(
    page_icon="💥",
    page_title="Jonis Task Managers",
    layout="centered"
)

st.title("Joni's Task Manager")

st.markdown("Herzlich willkommen in meiner **Task Manager App**. Hier können Tasks verwaltet werden, um sich selbst noch besser zu organisieren. **Hol das beste aus dir raus! 💯🔅✔**.")

due_date = st.date_input("Fälligkeitsdatum wählen")
reminder_date = st.date_input("Erinnerungsdatum wählen")
subject = st.text_input("Aufgabenbetreff eingeben")
description = st.text_area("Beschreibung einfügen")
priority = st.selectbox("Priorität wählen", ["Hoch", "Mittel", "Niedrig"])
done = st.checkbox("Erledigt")

print(due_date)



