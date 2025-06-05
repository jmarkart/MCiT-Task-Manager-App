import streamlit as st

st.set_page_config(
    page_title="Joni's Task Manager",
    page_icon="💥",
    layout="centered"
)

# Custom CSS für Headlines, Karten, Buttons, etc.
st.markdown("""
    <style>
    .big-title {
        font-size:2.5rem;
        font-weight:bold;
        color:#2940D3;
        margin-bottom:0.3em;
        letter-spacing: -1px;
    }
    .subtitle {
        font-size:1.3rem;
        color:#424242;
        margin-bottom:1.5em;
    }
    .feature-list {
        font-size:1.08rem;
        margin-bottom:2em;
    }
    .highlight-card {
        background: #F5F6FE;
        border-radius: 1.2em;
        padding: 1.3em 1.7em;
        margin-bottom: 1.3em;
        box-shadow: 0 2px 16px rgba(60,70,130,0.07);
        border: 1px solid #e6e7ee;
    }
    .motiv {
        margin-top:2em;
        font-style:italic;
        color:#999;
    }
    </style>
""", unsafe_allow_html=True)

# Headline
st.markdown('<div class="big-title">💥 Joni\'s Task Manager</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Deine Aufgaben, perfekt organisiert &mdash; produktiv, bunt, einfach!</div>', unsafe_allow_html=True)

# Features Block
st.markdown('''
<div class="highlight-card">
    <span style="font-size:1.5rem;">✨ <b>Das erwartet dich:</b></span>
    <ul class="feature-list">
        <li>📝 Aufgaben mit Priorität, Fälligkeit und Beschreibung anlegen</li>
        <li>🗂️ Kategorien wählen oder eigene Kategorien anlegen</li>
        <li>🔎 Aufgaben suchen, filtern und sortieren</li>
        <li>✅ Status einfach ändern: Offen, In Bearbeitung, Abgeschlossen</li>
        <li>📋 Übersichtliche Listen & Statistiken</li>
        <li>🌈 Modernes, einfaches Design</li>
    </ul>
</div>
''', unsafe_allow_html=True)

# Willkommen-Message
st.success("Starte direkt über das Menü links. Viel Erfolg beim Organisieren deiner Aufgaben! 💯")

# Tipp-Banner oder motivierendes Zitat
st.info("💡 **Tipp:** Du kannst jederzeit zwischen Aufgaben-Listen, Verwaltung und Suche wechseln.")

# Motivationsspruch
st.markdown("""
<div class="motiv">
    „Die einfachste Methode, den Tag zu strukturieren, ist, ihn zu planen.“
</div>
""", unsafe_allow_html=True)
