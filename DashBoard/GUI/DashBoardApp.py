import sys

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QProgressBar
from PyQt5.QtCore import *

SHOW_FULLSCREEN = False

try:
    # on Windows
    from DashBoard.GUI.AnalogueWidget.analoggaugewidget import AnalogGaugeWidget
except ImportError:
    # on Raspbian
    from AnalogueWidget.analoggaugewidget import AnalogGaugeWidget

    SHOW_FULLSCREEN = True

PROGRESS_BAR_STYLES = """
    QProgressBar{
        border: 2px solid grey;
        border-radius: 5px;
        text-align: center;
        background-color: black
    }
    QProgressBar::chunk {
        background-color: %s };
        width: 10px;
        margin: 1px;
    }
"""

INFO_LABEL_STYLES = """
    color: white;
    font-size: 20px;
    background-color: rgba(0,0,0,0%);
"""


class GUIContextData:
    """
    Simple struct which contains all needed to display data.
    """
    velocity = 0
    motor_speed = 0
    fuel_level = 0
    break_level = 0
    throttle_level = 0
    gearbox_state = "N"
    tcs_state = 1


class DashBoard(QMainWindow):
    """
    Main window class of PGR-05 Dashboard.
    Connection interface with other modules: update().
    """

    def __init__(self, width=800, height=480):
        super(DashBoard, self).__init__()

        self.setStyleSheet("background-color: 'black';")
        self.setFixedSize(width, height)

        self.context_data = GUIContextData()

        self.analog_size = int(self.width() * 0.4)  # 40% of screen width
        self.padding = 10

        # customisable widgets
        self.gearbox_label = QLabel(self)
        self.motor_speed_analog = AnalogGaugeWidget(self)
        self.velocity_analog = AnalogGaugeWidget(self)
        self.fuel_level_progressbar = QProgressBar(self)
        self.throttle_progressbar = QProgressBar(self)
        self.break_progressbar = QProgressBar(self)

        self.update_window()
        self.init_widgets()

        if SHOW_FULLSCREEN:
            self.showFullScreen()
        else:
            self.show()

    def update_window(self, velocity=0, motor_speed=0, gearbox_state="N", fuel_level=0, throttle_level=0,
                      break_level=0):
        if velocity in range(150):
            self.context_data.velocity = velocity
            self.velocity_analog.value = velocity

        if motor_speed in range(50):
            self.context_data.motor_speed = motor_speed
            self.motor_speed_analog.value = motor_speed

        if gearbox_state in ("N", "1", "2", "3", "4", "5"):
            GUIContextData.gearbox_state = gearbox_state
            self.gearbox_label.setText(gearbox_state)

        if fuel_level in range(100):
            self.context_data.fuel_level = fuel_level
            self.fuel_level_progressbar.setValue(fuel_level)

        if throttle_level in range(100):
            self.context_data.throttle_level = throttle_level
            self.throttle_progressbar.setValue(throttle_level)

        if break_level in range(100):
            self.context_data.break_level = break_level
            self.break_progressbar.setValue(break_level)

        self.update()

    def init_widgets(self):
        self.init_velocity_analog()
        self.init_motor_speed_analog()
        self.init_gearbox_label()
        self.init_fuel_level_progressbar()
        self.init_throttle_progressbar()
        self.init_break_progressbar()

        # region exit_button
        exit_button = QPushButton("X", self)
        exit_button.setFixedSize(20, 20)
        exit_button.clicked.connect(self.close)
        # endregion

    def init_velocity_analog(self):
        self.velocity_analog.move(self.padding, self.padding)
        self.velocity_analog.set_total_scale_angle_size(180)
        self.velocity_analog.set_MaxValue(150)
        self.velocity_analog.setFixedSize(self.analog_size, self.analog_size)

    def init_motor_speed_analog(self):
        self.motor_speed_analog.move(self.width() - self.analog_size - self.padding, self.padding)
        self.motor_speed_analog.set_total_scale_angle_size(180)
        self.motor_speed_analog.set_start_scale_angle(225)
        self.motor_speed_analog.set_MaxValue(50)
        self.motor_speed_analog.setFixedSize(self.analog_size, self.analog_size)

        multiply_label_styles = """
            color: white; font-size: 20px;
            background-color: rgba(0,0,0,0%)
        """
        multiply_label = QLabel(self)
        multiply_label.setStyleSheet(multiply_label_styles)
        multiply_label.setText("x100")
        multiply_label.move(self.width() - self.analog_size / 2, self.analog_size / 2 + 70)

    def init_gearbox_label(self):
        gearbox_label_styles = """
            color: white;
            font-size: 220px;
            background-color: rgba(0,0,0,0%);
        """
        # border: 3px inset gray;
        self.gearbox_label.setStyleSheet(gearbox_label_styles)
        self.gearbox_label.move(self.analog_size, self.padding)
        self.gearbox_label.setFixedSize(int(self.width() * 0.2), int(self.height() * 0.5))
        self.gearbox_label.setAlignment(Qt.AlignHCenter)

    def init_fuel_level_progressbar(self):
        bar_width = 300
        bar_height = 40
        self.fuel_level_progressbar.move(self.padding * 3, self.height() - 2 * self.padding - bar_height)
        self.fuel_level_progressbar.setFixedSize(bar_width, bar_height)
        self.fuel_level_progressbar.setStyleSheet(PROGRESS_BAR_STYLES % "red")
        self.fuel_level_progressbar.setTextVisible(False)

        info_label = QLabel(self)
        info_label.move(self.padding * 4 + bar_width, self.height() - 2 * self.padding - bar_height)
        info_label.setStyleSheet(INFO_LABEL_STYLES)
        info_label.setText("FUEL")

    def init_throttle_progressbar(self):
        bar_width = 300
        bar_height = 40
        self.throttle_progressbar.move(self.padding * 3, self.height() - 3 * self.padding - 2 * bar_height)
        self.throttle_progressbar.setFixedSize(bar_width, bar_height)
        self.throttle_progressbar.setStyleSheet(PROGRESS_BAR_STYLES % "blue")
        self.throttle_progressbar.setTextVisible(False)

        info_label = QLabel(self)
        info_label.move(self.padding * 4 + bar_width, self.height() - 3 * self.padding - 2 * bar_height)
        info_label.setStyleSheet(INFO_LABEL_STYLES)
        info_label.setText("THROTTLE")

    def init_break_progressbar(self):
        bar_width = 300
        bar_height = 40
        self.break_progressbar.move(self.padding * 3, self.height() - 4 * self.padding - 3 * bar_height)
        self.break_progressbar.setFixedSize(bar_width, bar_height)
        self.break_progressbar.setStyleSheet(PROGRESS_BAR_STYLES % "yellow")
        self.break_progressbar.setTextVisible(False)

        info_label = QLabel(self)
        info_label.move(self.padding * 4 + bar_width, self.height() - 4 * self.padding - 3 * bar_height)
        info_label.setStyleSheet(INFO_LABEL_STYLES)
        info_label.setText("BREAK")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()
    # window = DashBoard(screen_resolution.width(), screen_resolution.height())
    window = DashBoard()
    app.exec_()
