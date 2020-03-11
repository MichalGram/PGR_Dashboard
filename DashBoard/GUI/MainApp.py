import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # self.setGeometry(0, 0, 800, 400)
        self.setWindowTitle("6")

        label = QLabel("6")
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)
        self.showFullScreen()


app = QApplication(sys.argv)
window = MainWindow()
app.exec_()
