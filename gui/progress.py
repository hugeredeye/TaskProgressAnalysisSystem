from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class ProgressWidget(QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Progress')
        self.resize(600, 400)

        self.layout = QVBoxLayout()

        # Create matplotlib figure and canvas
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)
        self.layout.addWidget(self.canvas)

        self.setLayout(self.layout)

        # Plot the progress
        self.plot_progress()

    def plot_progress(self):
        # Get task data from the database
        tasks = self.db.get_tasks()
        completed_tasks = sum(1 for task in tasks if task[4] == 'Completed')
        pending_tasks = sum(1 for task in tasks if task[4] == 'Pending')

        # Create a pie chart
        labels = ['Completed', 'Pending']
        sizes = [completed_tasks, pending_tasks]
        colors = ['lightgreen', 'lightcoral']
        explode = (0.1, 0)  # explode the first slice (completed tasks)

        self.ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        self.ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

        # Redraw the canvas
        self.canvas.draw()
