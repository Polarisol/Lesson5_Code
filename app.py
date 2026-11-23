import sys

from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Lesson 5")

        self.spinbox = QSpinBox()
        self.spinbox.setRange(0, 10000)
        self.spinbox.setReadOnly(True)
        self.spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinbox.setStyleSheet("background-color: lightgray;")

        self.button = QPushButton("Start")
        self.button.setCheckable(True)
        self.button.toggled.connect(self.button_method)

        layout = QVBoxLayout()
        layout.addWidget(self.spinbox)
        layout.addWidget(self.button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def button_method(self, checked: bool) -> None:
        self.button.setText("Stop" if checked else "Start")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
