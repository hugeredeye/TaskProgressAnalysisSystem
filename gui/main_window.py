from PyQt5.QtWidgets import QMainWindow, QAction, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QDateEdit, QComboBox, QLabel, QHBoxLayout, QPushButton, QTabWidget, QCalendarWidget, QMenu, QMessageBox
from PyQt5.QtCore import QDate, Qt
from gui.add_task import AddTaskWidget
from gui.analytics import AnalyticsWidget
from gui.progress import ProgressWidget

class MainWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Task Manager')
        self.resize(1200, 800)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        addTaskAction = QAction('Add Task', self)
        addTaskAction.triggered.connect(self.showAddTaskTab)
        fileMenu.addAction(addTaskAction)

        analyticsAction = QAction('Analytics', self)
        analyticsAction.triggered.connect(self.showAnalyticsTab)
        fileMenu.addAction(analyticsAction)

        progressAction = QAction('Progress', self)
        progressAction.triggered.connect(self.showProgressTab)
        fileMenu.addAction(progressAction)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Add Calendar widget
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.showDayTasks)

        # Add tasks table
        self.tasks_table = QTableWidget()
        self.tasks_table.setColumnCount(8)
        self.tasks_table.setHorizontalHeaderLabels(['ID', 'Title', 'Description', 'Due Date', 'Status', 'Priority', 'Category', 'Comment'])
        self.tasks_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tasks_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tasks_table.customContextMenuRequested.connect(self.openMenu)

        # Add tasks tab
        self.tasks_tab_layout = QVBoxLayout()
        self.tasks_tab_layout.addWidget(self.calendar)
        self.tasks_tab_layout.addWidget(self.tasks_table)
        self.tasks_tab = QWidget()
        self.tasks_tab.setLayout(self.tasks_tab_layout)
        self.tabs.addTab(self.tasks_tab, "Tasks")

    def showDayTasks(self):
        selected_date = self.calendar.selectedDate()
        tasks = self.db.get_tasks_for_date(selected_date)
        self.tasks_table.setRowCount(len(tasks))
        for row, task in enumerate(tasks):
            for column, data in enumerate(task):
                self.tasks_table.setItem(row, column, QTableWidgetItem(str(data)))

    def showAddTaskTab(self, task_id=None):
        add_task_widget = AddTaskWidget(self.db, task_id)
        add_task_widget.task_added.connect(self.loadTasks)
        self.tabs.addTab(add_task_widget, "Add/Edit Task")
        self.tabs.setCurrentWidget(add_task_widget)

    def showAnalyticsTab(self):
        analytics_widget = AnalyticsWidget(self.db)
        self.tabs.addTab(analytics_widget, "Analytics")
        self.tabs.setCurrentWidget(analytics_widget)

    def showProgressTab(self):
        progress_widget = ProgressWidget(self.db)
        self.tabs.addTab(progress_widget, "Progress")
        self.tabs.setCurrentWidget(progress_widget)

    def loadTasks(self):
        self.showDayTasks()

    def openMenu(self, position):
        print(2)
        menu = QMenu()

        edit_action = QAction('Edit', self)
        edit_action.triggered.connect(self.editTask)
        menu.addAction(edit_action)

        delete_action = QAction('Delete', self)
        delete_action.triggered.connect(self.deleteTask)
        menu.addAction(delete_action)

        menu.exec_(self.tasks_table.viewport().mapToGlobal(position))

    def editTask(self):
        current_row = self.tasks_table.currentRow()
        if current_row < 0:
            return
        task_id = self.tasks_table.item(current_row, 0).text()
        self.showAddTaskTab(task_id)

    def deleteTask(self):
        current_row = self.tasks_table.currentRow()
        if current_row < 0:
            return
        task_id = self.tasks_table.item(current_row, 0).text()
        confirm = QMessageBox.question(self, 'Delete Task', f'Are you sure you want to delete Task ID: {task_id}?', QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.db.delete_task(task_id)
            self.loadTasks()  # Refresh the table
            QMessageBox.information(self, 'Task Deleted', f'Task ID: {task_id} has been deleted.')



def main():
    # Создание приложения
    app = QApplication(sys.argv)

    # Установка шрифта для всего приложения
    font = QFont("Bookman Old Style", 16)
    app.setFont(font)

    # Инициализация базы данных
    db = DBHelper()

    # Создание и отображение основного окна
    main_window = MainWindow(db)
    main_window.show()

    # Запуск приложения
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
