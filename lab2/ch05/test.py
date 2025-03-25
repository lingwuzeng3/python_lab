from PySide6.QtWidgets import QApplication,QWidget,QTextEdit

class Window(QWidget):
    def __init__(self):
        super().__init__()



if __name__ == "__main__":
    app = QApplication()
    my_window = Window()
    my_window.show()
    app.exec()
