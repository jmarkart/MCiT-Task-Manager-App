import streamlit as st

st.title("Überblick")

if "tasks" not in st.session_state or not st.session_state["tasks"]:
    st.info("Noch keine Aufgaben vorhanden.")
else:
    tasks = st.session_state["tasks"]
    anzahl_gesamt = len(tasks)
    offen = sum(1 for t in tasks if t["Status"] == "Offen")
    in_bearbeitung = sum(1 for t in tasks if t["Status"] == "In Bearbeitung")
    abgeschlossen = sum(1 for t in tasks if t["Status"] == "Abgeschlossen")

    st.metric("Gesamtzahl Aufgaben", anzahl_gesamt)
    st.metric("Offen", offen)
    st.metric("In Bearbeitung", in_bearbeitung)
    st.metric("Abgeschlossen", abgeschlossen)

    # Optional: Aufgaben nach Kategorie
    st.subheader("Aufgaben nach Kategorie")
    from collections import Counter
    kategorie_counter = Counter([t["Kategorie"] for t in tasks if t.get("Kategorie")])
    if kategorie_counter:
        st.table(kategorie_counter.most_common())
    else:
        st.info("Noch keine Kategorien erfasst.")

    # Optional: Diagramm
    try:
        import matplotlib.pyplot as plt

        labels = ["Offen", "In Bearbeitung", "Abgeschlossen"]
        values = [offen, in_bearbeitung, abgeschlossen]
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)
    except ImportError:
        st.info("matplotlib nicht installiert, kein Diagramm angezeigt.")
