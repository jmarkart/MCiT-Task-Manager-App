def search_tasks(tasks, search_query):
    """
    Filtert die Aufgabenliste nach Suchbegriff im Betreff, der Beschreibung oder der Kategorie.
    """
    if not search_query:
        return tasks
    query = search_query.lower()
    return [
        task for task in tasks
        if query in task['Betreff'].lower()
        or query in task['Beschreibung'].lower()
        or query in task['Kategorie'].lower()
    ]
