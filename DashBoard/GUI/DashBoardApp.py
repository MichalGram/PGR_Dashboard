import sys, time

from DashBoard.GUI.AnalogueWidget.analoggaugewidget import AnalogGaugeWidget
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton

'''
Main window class of PGR-05 Dashboard.
'''


class DashBoard(QMainWindow):
    def __init__(self, width=800, height=480):
        super(DashBoard, self).__init__()

        self.setStyleSheet("background-color: 'black';")
        self.setFixedSize(width, height)

        #region exit_button
        exit_button = QPushButton("X", self)
        exit_button.setFixedSize(20, 20)
        exit_button.clicked.connect(self.change_motor_speed)
        #endregion

        self.init_fields()
        self.showFullScreen()

    def change_motor_speed(self):
        self.motor_speed_analog.value = 500
        self.velocity_analog.value = 50
        self.update()

    def init_fields(self):
        def init_velocity_analog(self):
            self.velocity_analog.move(10, 10)
            self.velocity_analog.set_total_scale_angle_size(180)
            self.velocity_analog.set_MaxValue(150)
            self.velocity_analog.setFixedSize(self.analog_size, self.analog_size)

        def init_motor_speed_analog(self):
            self.motor_speed_analog.move(self.width() - self.analog_size - 10, 10)
            self.motor_speed_analog.set_total_scale_angle_size(180)
            self.motor_speed_analog.set_start_scale_angle(225)
            self.motor_speed_analog.set_MaxValue(5000)
            self.motor_speed_analog.setFixedSize(self.analog_size, self.analog_size)

        def init_gearbox_label(self):
            self.gearbox_label.setStyleSheet("border: 3px inset gray;")
            self.gearbox_label.move(self.analog_size + 20, 10)
            self.gearbox_label.setFixedSize(int(self.width() * 0.2 - 40), int(self.height() * 0.4))


        self.analog_size = int(self.width() * (0.4)) # 40% of screen width

        self.velocity_analog = AnalogGaugeWidget(self)
        init_velocity_analog(self)

        self.motor_speed_analog = AnalogGaugeWidget(self)
        init_motor_speed_analog(self)

        self.gearbox_label = QLabel(self)
        init_gearbox_label(self)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()
    window = DashBoard(screen_resolution.width(), screen_resolution.height())
    # window = DashBoard()
    app.exec_()
