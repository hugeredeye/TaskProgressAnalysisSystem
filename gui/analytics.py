from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QDateEdit, QPushButton
from PyQt5.QtCore import Qt, QDate

class AnalyticsWidget(QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        # Date selection
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())
        self.layout.addWidget(self.date_edit)

        # Button to trigger analysis
        self.analyze_button = QPushButton('Analyze', self)
        self.analyze_button.clicked.connect(self.analyze)
        self.layout.addWidget(self.analyze_button)

        # Result label
        self.result_label = QLabel()
        self.layout.addWidget(self.result_label)

        # Set layout
        self.setLayout(self.layout)

    def analyze(self):
        selected_date = self.date_edit.date().toString('yyyy-MM-dd')

        # Get tasks from the database for the selected date
        tasks = self.db.get_tasks_for_date(selected_date)

        # Display statistics for the selected date
        self.result_label.setText(f"Analysis for {selected_date}:")
        self.result_label.setAlignment(Qt.AlignCenter)

        total_tasks = len(tasks)
        completed_tasks = sum(1 for task in tasks if task[4] == 'Completed')
        pending_tasks = total_tasks - completed_tasks

        self.result_label.setText(
            f"Total tasks: {total_tasks}\n"
            f"Completed tasks: {completed_tasks}\n"
            f"Pending tasks: {pending_tasks}"
        )

