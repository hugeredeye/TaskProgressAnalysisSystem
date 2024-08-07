This project is a PyQt5-based "Task Manager" application that uses an SQLite database to manage tasks. It allows users to add, edit, and delete tasks, as well as view analytics and track progress.

The project consists of several components:
1. **Main.py**: The main file that starts the application.
2. **Database folder**: A module for interacting with the SQLite database.
3. **GUI folder**: Modules for creating the user interface, including adding tasks, viewing analytics, and tracking progress.
   
Other important files include:
- stylesheets: CSS files for styling the application's interface.- Icons - Images for icons used in the app
- loadTasks: Method for loading tasks.
- openMenu: Method for opening the menu.
- editTask: Method for editing tasks.
- deleteTask: Method for deleting tasks.

Basic Methods
- showDayTasks: Shows tasks for the selected date.
- showAddTaskTab: Opens a tab for adding or editing tasks.
- ShowAnalyticsTab: Opens the analytics tab.
- showsProgressTab: Opens progress tab.
loadTasks re-loads the tasks.
openMenu opens the context menu for editing or deleting tasks. 
editTask opens the selected task for editing. 
deleteTask deletes the selected task after confirmation.

Main Application Launch Function
1. Creates QApplication object. 
2. Initializes database. 
3. Creates and displays main window. 
4. Starts application event loop. 

Database/DB_Helper.py 
This file contains a class for a SQLite database. 
basic methods
createTables creates tables if they do not exist. 
addTask adds a new task to the database. 
get_tasks returns all tasks from the database. 
get_task returns the task by id. 
update_task updates an existing task.- delete_task(): Deletes a task with the specified ID.

gui/add_task.py
- AddTaskWidget: Widget for adding, editing and deleting tasks
  - initUI()
  - load_task()
  save_task() 
gui.analytics.py 

- AnalyticsWidget: Displays analytics
  - analyze()
ProgressWidget: Displays progress
initUI()
plot_progress()**Project Overview**
This project is a task management application built with PyQt5 and SQLite, designed to help users manage their tasks in a simple and efficient manner. The main features of the application include:
- Task creation and editing
- Priority system
- Reminders
- Due dates
- Notifications
**Installation**
To run the project, you will need to install the following dependencies:
```python
pip install pyqt5 matplotlib
```

Once the dependencies are installed, you can run the application by running the `main.py` file:
```bash
python main.py
```

**Project Structure**
The project consists of two main files: `gui/main_window.py` and `main.py`. `main.py` is the main entry point for the application and contains the main logic of the program. `gui/main_window.py` contains the GUI (Graphical User Interface) for the application.
Both files can be merged or deleted to simplify the project structure if desired.

**Conclusion**
In this project, we have created a simple but functional task management application using Python, PyQt5, and SQLite. The application allows users to create, edit, and manage tasks with ease.
By following this guide, you should now have a good understanding of the structure and components of the project and how to make changes or additions to the code.
