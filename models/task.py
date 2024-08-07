# Модель задачи
class Task:
    def __init__(self, title, description, due_date, status, priority, category, comment):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.priority = priority
        self.category = category
        self.comment = comment
