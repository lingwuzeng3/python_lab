import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import QRectF

class OlympicRingsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Olympic Rings")
        self.resize(400, 200)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 设置抗锯齿

        # 定义五环的颜色
        colors = [QColor("blue"), QColor("black"), QColor("red"), QColor("yellow"), QColor("green")]

        # 定义五环的位置和大小
        rings = [
            QRectF(50, 50, 100, 100),
            QRectF(150, 50, 100, 100),
            QRectF(250, 50, 100, 100),
            QRectF(100, 100, 100, 100),
            QRectF(200, 100, 100, 100)
        ]

        # 绘制五环
        for i, ring in enumerate(rings):
            painter.setPen(colors[i])
            painter.drawEllipse(ring)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OlympicRingsWidget()
    window.show()
    sys.exit(app.exec())
