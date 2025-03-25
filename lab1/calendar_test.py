'''结合PySide6实现具有GUI界面的简单日历和时间显示的应用，提交源代码和运行截图。'''
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCalendarWidget
from PySide6.QtCore import QTime, QDate, QTimer
import sys

class CalendarApp(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.calendar = QCalendarWidget()
        self.layout.addWidget(self.calendar)

        self.time_label = QLabel()
        self.layout.addWidget(self.time_label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString()
        current_date = QDate.currentDate().toString()
        self.time_label.setText("Date: {} | Time: {}".format(current_date, current_time))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarApp()
    window.show()
    sys.exit(app.exec())
