# 💥 Joni's Task Manager

Willkommen zu **Joni's Task Manager** – deiner modernen Web-App zur Aufgabenverwaltung!

Mit diesem Tool kannst du Aufgaben schnell und flexibel erfassen, kategorisieren, filtern, durchsuchen, im Kalender anzeigen und mit Notizen sowie Anhängen ausstatten. Bleib organisiert – egal ob Uni, Arbeit oder Privatleben!

---

## ✨ Features

* **Aufgaben anlegen** mit Fälligkeit, Erinnerung, Priorität, Kategorie, Beschreibung
* **Eigene oder vorgeschlagene Kategorien** (z. B. Uni, Arbeit, Privat)
* **Status-Management**: Offen, In Bearbeitung, Abgeschlossen
* **Aufgaben filtern und sortieren** nach Kategorie, Status und Priorität
* **Suchfunktion** für Aufgaben und Kategorien
* **Notizen und Anhänge** (PDF-Upload, externe Links) zu Aufgaben speichern
* **Kalenderansicht** aller Aufgaben inkl. Klick für Details
* **Multi-Page Aufbau**: Aufgaben verwalten, Aufgabenliste, Suche, Kalender u. v. m.

---

## 🚀 Installation

1.  **Repository klonen:**
    ```bash
    git clone <dein-repo-link>
    cd jonis_task_manager
    ```

2.  **Abhängigkeiten installieren:**
    ```bash
    pip install -r requirements.txt
    ```

    **Hinweis:** Für die Kalenderansicht wird das Paket `streamlit-calendar` benötigt (ist in `requirements.txt` enthalten).

---



## Projektstruktur

```text
MCiT-Task-Manager-App/
│
├── Code/
│   ├── home.py                      # Startseite
│   ├── pages/
│   │   ├── 1_Aufgaben_Verwalten.py  # Aufgaben erfassen
│   │   ├── 2_Aufgaben_Liste.py      # Aufgabenliste und Status
│   │   ├── 3_Suche.py               # Suchen & filtern
│   │   ├── 4_Kalender.py            # Kalenderansicht
│   ├── task_utils.py                # Logik rund um Aufgaben
│   ├── category_utils.py            # Kategorien-Logik
│   ├── status_utils.py              # Status-Optionen
│   ├── search_utils.py              # Suchfunktion
│   ├── attachment_utils.py          # Notizen & Anhänge
│
├── requirements.txt                 # Abhängigkeiten
├── .gitignore                       # Git Ignore
└── README.md                        # Diese Projektbeschreibung
