# Joni's Task Manager

Willkommen zu **Joni's Task Manager**!  
Mit dieser App organisierst du Aufgaben einfach per Weboberfläche, kannst Kategorien und Status zuweisen, filtern, suchen und vieles mehr.

---

## Features

- Aufgaben anlegen mit Fälligkeitsdatum, Erinnerung, Priorität, Beschreibung und Kategorie
- Kategorien frei wählbar oder aus Vorschlägen (z.B. Uni, Arbeit, Privat)
- Status-Management: Offen, In Bearbeitung, Abgeschlossen
- Aufgaben nach Kategorie filtern
- Suchfunktion für Aufgaben und Kategorien
- Übersicht zu aktiven und abgeschlossenen Aufgaben

---

## Projektstruktur

```text
jonis_task_manager/
│
├── code/
│   ├── main.py             # Startpunkt der App
│   ├── task_utils.py       # Aufgabenfunktionen
│   ├── category_utils.py   # Kategorien-Funktionen
│   ├── status_utils.py     # Status-Optionen & Icons
│   └── search_utils.py     # Suchfunktion
│
├── .gitignore              # Git Ignore File
├── requirements.txt        # Python-Abhängigkeiten
└── README.md               # Diese Projektbeschreibung


