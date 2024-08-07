# Класс для взаимодействия с базой данных
import sqlite3
from sqlalchemy.exc import SQLAlchemyError


class DBHelper:
    def __init__(self, dbname="tasks.db"):
        self.conn = sqlite3.connect(dbname)
        self.create_tables()

    def create_tables(self):
        """users_query =
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL
        ); """
        tasks_query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT NOT NULL,
            status TEXT NOT NULL,
            priority TEXT NOT NULL,
            category TEXT NOT NULL,
            comment TEXT
        );
        """
        # self.conn.execute(users_query)
        self.conn.execute(tasks_query)
        self.conn.commit()

        # def add_user(self, name, email, phone):
        # query = "INSERT INTO users (name, email, phone) VALUES (?, ?, ?);"
        # self.conn.execute(query, (name, email, phone))
        # self.conn.commit()

    # def get_users(self):
    #     query = "SELECT * FROM users;"
    #     cursor = self.conn.execute(query)
    #     users = cursor.fetchall()
    #     return users

    def add_task(self, title, description, due_date, status, priority, category, comment):
        query = "INSERT INTO tasks (title, description, due_date, status, priority, category, comment) VALUES (?, ?, ?, ?, ?, ?, ?);"
        self.conn.execute(query, (title, description, due_date, status, priority, category, comment))
        self.conn.commit()

    def get_tasks(self):
        query = "SELECT * FROM tasks;"
        cursor = self.conn.execute(query)
        tasks = cursor.fetchall()
        return tasks

    def get_task(self, task_id):
        query = "SELECT * FROM tasks WHERE id = ?;"
        cursor = self.conn.execute(query, (task_id,))
        task = cursor.fetchone()
        return task

    def update_task(self, task_id, title, description, due_date, status, priority, category, comment):
        query = "UPDATE tasks SET title = ?, description = ?, due_date = ?, status = ?, priority = ?, category = ?, comment = ? WHERE id = ?;"
        self.conn.execute(query, (title, description, due_date, status, priority, category, comment, task_id))
        self.conn.commit()

    def delete_task(self, task_id):
        query = "DELETE FROM tasks WHERE id = ?;"
        self.conn.execute(query, (task_id,))
        self.conn.commit()

    def get_tasks_for_date(self, selected_date):
        query = '''
        SELECT * FROM tasks WHERE due_date = ?
        '''
        tasks = self.conn.execute(query, (selected_date, )).fetchall()
        return tasks

    # def get_user_by_name(self, name):
    #     try:
    #         print(name)
    #         return False # self.session.query(User).filter(User.name == name).one()
    #     except SQLAlchemyError as e:
    #         print(f"Ошибка получения пользователя по имени: {e}")
    #         return None
