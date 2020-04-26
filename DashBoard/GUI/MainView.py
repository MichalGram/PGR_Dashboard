try:
    from DashBoard.GUI.styles import *
except:
    from GUI.styles import *

from PyQt5 import QtCore
from PyQt5.QtWidgets import QLCDNumber, QLabel, QProgressBar, QWidget


class MainView(QWidget):
    def __init__(self, main_window):
        super(MainView, self).__init__()

        self.setFixedSize(main_window.width(), main_window.height())

        self.gear_LCD = QLCDNumber(main_window)
        self.init_gear_LCD()

        self.rpm_progressbar = QProgressBar(main_window)
        self.init_rpm_progressbar()

        self.break_progressbar = QProgressBar(main_window)
        self.init_break_progressbar()

        self.rpm_LCD = QLCDNumber(main_window)
        self.label_rpm = QLabel(main_window)
        self.init_rpm_LCD()

        self.speed_LCD = QLCDNumber(main_window)
        self.label_speed = QLabel(main_window)
        self.init_speed_LCD()

        self.water_temp_label = QLabel(main_window)
        self.init_water_temp()

        self.oil_temp_label = QLabel(main_window)
        self.init_oil_temp()

        self.RTCS_mode_label = QLabel(main_window)
        self.init_RTCS_mode()

    def init_gear_LCD(self):
        self.gear_LCD.setDigitCount(1)
        self.gear_LCD.setFixedSize(int(self.width() * 0.25), self.height() * 0.625)
        self.gear_LCD.move(int(self.width() * 0.60), 0)
        self.gear_LCD.display(0)
        self.gear_LCD.setStyleSheet(WHITE_FONT)

    def init_rpm_progressbar(self):
        self.rpm_progressbar.setOrientation(QtCore.Qt.Vertical)
        self.rpm_progressbar.setFixedSize(int(self.width() * 0.05), int(self.height() - 2 * OFFSET))
        self.rpm_progressbar.move(OFFSET, OFFSET)
        self.rpm_progressbar.setStyleSheet(PROGRESS_BAR_STYLES % ("white", "white"))
        self.rpm_progressbar.setValue(80)
        self.rpm_progressbar.setTextVisible(False)

    def init_break_progressbar(self):
        self.break_progressbar.setOrientation(QtCore.Qt.Vertical)
        self.break_progressbar.setFixedSize(int(self.width() * 0.05), int(0.5 * self.height()))
        self.break_progressbar.move(self.width() - self.break_progressbar.width() - OFFSET, 0.25 * self.height())
        self.break_progressbar.setStyleSheet(PROGRESS_BAR_STYLES % ("yellow", "yellow"))
        self.break_progressbar.setValue(80)
        self.break_progressbar.setTextVisible(False)

    def init_rpm_LCD(self, ):
        self.rpm_LCD.setDigitCount(4)
        self.rpm_LCD.setFixedSize(int(self.width() * 0.35), self.height() * 0.25)
        self.rpm_LCD.move(2 * OFFSET + self.rpm_progressbar.width(), OFFSET)
        self.rpm_LCD.display(9000)
        self.rpm_LCD.setStyleSheet(WHITE_FONT + TRANSPARENT_BACKGROUND)

        self.label_rpm.setText('RPM')
        self.label_rpm.setFixedSize(self.width() * 0.15, self.rpm_LCD.height())
        self.label_rpm.move(2 * OFFSET + self.rpm_progressbar.width() + self.rpm_LCD.width(), OFFSET)
        self.label_rpm.setStyleSheet(INFO_LABEL_STYLES)

    def init_speed_LCD(self):
        self.speed_LCD.setDigitCount(3)
        self.speed_LCD.setFixedSize(int(self.width() * 0.35), self.height() * 0.25)
        self.speed_LCD.move(2 * OFFSET + self.rpm_progressbar.width(), self.rpm_LCD.height() + 2 * OFFSET)
        self.speed_LCD.display(20)
        self.speed_LCD.setStyleSheet(WHITE_FONT)

        self.label_speed.setText('SPD')
        self.label_speed.setFixedSize(self.width() * 0.15, self.speed_LCD.height())
        self.label_speed.move(2 * OFFSET + self.rpm_progressbar.width() + self.speed_LCD.width(),
                              self.rpm_LCD.height() + 2 * OFFSET)
        self.label_speed.setStyleSheet(INFO_LABEL_STYLES)

    def init_water_temp(self):
        self.water_temp_label.setFixedSize(self.width() * 0.25, self.height() * 0.3)
        self.water_temp_label.move(self.rpm_progressbar.width() + 2 * OFFSET,
                                   self.height() - self.water_temp_label.height() - OFFSET)
        self.water_temp_label.setStyleSheet(STATUS_LABEL_STYLES % (self.height() / 10, 'blue'))
        self.water_temp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.water_temp_label.setText("WATER:\n100°C")

    def init_oil_temp(self):
        self.oil_temp_label.setFixedSize(self.width() * 0.25, self.height() * 0.3)
        self.oil_temp_label.move(self.rpm_progressbar.width() + self.water_temp_label.width() + 3 * OFFSET,
                                 self.height() - self.oil_temp_label.height() - OFFSET)
        self.oil_temp_label.setStyleSheet(STATUS_LABEL_STYLES % (self.height() / 10, 'darkorange'))
        self.oil_temp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.oil_temp_label.setText("OIL:\n100°C")

    def init_RTCS_mode(self):
        self.RTCS_mode_label.setFixedSize(self.width() * 0.25, self.height() * 0.3)
        self.RTCS_mode_label.move(self.rpm_progressbar.width() + 2 * self.water_temp_label.width() + 4 * OFFSET,
                                  self.height() - self.oil_temp_label.height() - OFFSET)
        self.RTCS_mode_label.setStyleSheet(STATUS_LABEL_STYLES % (self.height() / 10, 'yellow'))
        self.RTCS_mode_label.setAlignment(QtCore.Qt.AlignCenter)
        self.RTCS_mode_label.setText("RTCS:\n1")

    def update_main_view(self, display_info):
        self.gear_LCD.display(display_info.gear)
        self.rpm_progressbar.setValue(display_info.rpm)
        self.rpm_LCD.display(display_info.rpm)
        self.break_progressbar.setValue(display_info.break_balance)
        self.speed_LCD.display(display_info.speed)
        self.water_temp_label.setText("WATER:\n{}°C".format(display_info.water_temp))
        self.oil_temp_label.setText("OIL:\n{}°C".format(display_info.oil_temp))
        self.RTCS_mode_label.setText("RTCS:\n{}".format(display_info.race_tcs_mode))

    def setVisible(self, visibility):
        self.gear_LCD.setVisible(visibility)
        self.rpm_progressbar.setVisible(visibility)
        self.break_progressbar.setVisible(visibility)
        self.rpm_LCD.setVisible(visibility)
        self.speed_LCD.setVisible(visibility)
        self.label_rpm.setVisible(visibility)
        self.label_speed.setVisible(visibility)
        self.water_temp_label.setVisible(visibility)
        self.oil_temp_label.setVisible(visibility)
        self.RTCS_mode_label.setVisible(visibility)
