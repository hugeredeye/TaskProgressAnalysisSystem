from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QComboBox, QDateEdit, QPushButton
from PyQt5.QtCore import pyqtSignal, QDate


class AddTaskWidget(QWidget):
    task_added = pyqtSignal()

    def __init__(self, db, task_id=None):
        super().__init__()
        self.db = db
        self.task_id = task_id
        self.initUI()
        if task_id:
            self.loadTask(task_id)

    def initUI(self):
        layout = QVBoxLayout()

        self.title_edit = QLineEdit()
        self.description_edit = QTextEdit()
        self.due_date_edit = QDateEdit()
        self.due_date_edit.setCalendarPopup(True)
        self.due_date_edit.setDate(QDate.currentDate())
        self.status_combo = QComboBox()
        self.status_combo.addItems(['Pending', 'Completed'])
        self.priority_combo = QComboBox()
        self.priority_combo.addItems(['Low', 'Medium', 'High'])
        self.category_edit = QLineEdit()
        self.comment_edit = QTextEdit()

        layout.addWidget(QLabel('Title'))
        layout.addWidget(self.title_edit)
        layout.addWidget(QLabel('Description'))
        layout.addWidget(self.description_edit)
        layout.addWidget(QLabel('Due Date'))
        layout.addWidget(self.due_date_edit)
        layout.addWidget(QLabel('Status'))
        layout.addWidget(self.status_combo)
        layout.addWidget(QLabel('Priority'))
        layout.addWidget(self.priority_combo)
        layout.addWidget(QLabel('Category'))
        layout.addWidget(self.category_edit)
        layout.addWidget(QLabel('Comment'))
        layout.addWidget(self.comment_edit)

        self.save_button = QPushButton('Save Task')
        self.save_button.clicked.connect(self.saveTask)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def loadTask(self, task_id):
        task = self.db.get_task(task_id)
        if task:
            self.title_edit.setText(task[1])
            self.description_edit.setText(task[2])
            self.due_date_edit.setDate(QDate.fromString(task[3], 'yyyy-MM-dd'))
            self.status_combo.setCurrentText(task[4])
            self.priority_combo.setCurrentText(task[5])
            self.category_edit.setText(task[6])
            self.comment_edit.setText(task[7])

    def saveTask(self):
        title = self.title_edit.text()
        description = self.description_edit.toPlainText()
        due_date = self.due_date_edit.date().toString('yyyy-MM-dd')
        status = self.status_combo.currentText()
        priority = self.priority_combo.currentText()
        category = self.category_edit.text()
        comment = self.comment_edit.toPlainText()

        if self.task_id:
            self.db.update_task(self.task_id, title, description, due_date, status, priority, category, comment)
        else:
            self.db.add_task(title, description, due_date, status, priority, category, comment)

        self.task_added.emit()
        self.close()

