import sys

from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from PySide6.QtCore import Qt, QTimer


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Lesson 5")

        self.counter = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_method)

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

        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setRange(0,255)
        self.slider_spinbox = QSpinBox()
        self.slider_spinbox.setRange(self.slider.minimum(), self.slider.maximum())
        self.slider_spinbox.setReadOnly(True)
        self.slider_spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.slider_spinbox.setStyleSheet("background-color: lightgray;")
        self.slider.valueChanged.connect(self.slider_method)

        slider_layout = QVBoxLayout()
        slider_layout.addWidget(self.slider_spinbox)
        slider_layout.addWidget(self.slider)

        main_layout = QHBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addLayout(slider_layout)
        self.color_box = QLabel()
        self.color_box.setMinimumWidth(100)
        self.color_box.setStyleSheet('background-color: rgb(0,0,0)')
        main_layout.addWidget(self.color_box)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def button_method(self, checked: bool) -> None:
        self.button.setText("Stop" if checked else "Start")
        if checked:
            self.timer.start(10)
        else:
            self.timer.stop()

    def timer_method(self):
        self.counter += 1
        self.spinbox.setValue(self.counter)
        if self.counter == 500:
            self.timer.stop()
            self.button.setChecked(False)

    def slider_method(self):
        value = self.slider.value()
        self.slider_spinbox.setValue(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
