import sys

try:
    import RPi.GPIO as GPIO
    print('GPIO imported!')
except:
    print("GPIO import went wrong...")

try:
    from DashBoard.GUI.MainView import MainView
    SHOW_FULLSCREEN = False
except:
    from GUI.MainView import MainView
    SHOW_FULLSCREEN = True

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow




class BolideInfo:
    gear = 0
    rpm = 0
    break_balance = 0
    speed = 0
    water_temp = 0
    oil_temp = 0
    race_tcs_mode = 0


class DashBoard(QMainWindow):
    def __init__(self, screen_width=800, screen_height=480):
        super(DashBoard, self).__init__()

        self.setStyleSheet("background-color: black")
        self.setFixedSize(screen_width, screen_height)

        self.bolide_info = BolideInfo()
        self.main_view = MainView(self)

        if SHOW_FULLSCREEN:
            self.showFullScreen()
        else:
            self.show()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Q:
            self.close()
        elif event.key() == QtCore.Qt.Key_W:
            self.main_view.setVisible(True)
        elif event.key() == QtCore.Qt.Key_E:
            self.main_view.setVisible(False)
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    try:
        GPIO.setmode(GPIO.BCM)
    except:
        print("Running on windows")


    if SHOW_FULLSCREEN:
        size = app.desktop().screenGeometry()
        width, height = size.width(), size.height()
        window = DashBoard(width, height)
    else:
        window = DashBoard()

    app.exec_()
