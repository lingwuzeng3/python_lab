import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('简单计算器')
        self.setGeometry(100, 100, 300, 400)

        # 创建垂直布局
        layout = QVBoxLayout()

        # 创建显示结果的文本框
        self.display = QLineEdit(self)
        self.display.setFixedHeight(50)
        self.display.setReadOnly(True)
        layout.addWidget(self.display)

        # 创建按钮布局
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row in buttons:
            h_layout = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text, self)
                button.setFixedSize(60, 60)
                button.clicked.connect(self.on_button_click)
                h_layout.addWidget(button)
            layout.addLayout(h_layout)

        # 设置布局
        self.setLayout(layout)

    def on_button_click(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception as e:
                self.display.setText("错误")
        else:
            self.display.setText(self.display.text() + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = CalculatorApp()
    calc.show()
    sys.exit(app.exec())