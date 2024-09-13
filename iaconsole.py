# PyQt5 introduction
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout, QVBoxLayout, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("iaconsole")
        self.setGeometry(500, 100, 408, 826)
        self.setWindowOpacity(0.0)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint)
        self.initUI()

    def initUI(self):
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        centralWidgetGridLayout = QGridLayout()

        backgroundImage = QPixmap("assets/iaconsole-bg.png")
        backgroundLabel = QLabel("iaconsole", self)
        backgroundLabel.setPixmap(backgroundImage)

        centralWidgetGridLayout.addWidget(backgroundLabel, 0, 0)

        foregroundWidget = QWidget(self)
        foregroundWidget.setStyleSheet("margin: 60px 19px 50px 21px;")
        centralWidgetGridLayout.addWidget(foregroundWidget, 0, 0)

        foregroundWidgetGridLayout = QGridLayout()
        foregroundWidgetGridLayout.setContentsMargins(0, 0, 0, 0)
        foregroundWidgetGridLayout.setHorizontalSpacing(0)
        foregroundWidgetGridLayout.setVerticalSpacing(0)
        foregroundWidgetGridLayout.setRowStretch(0, 0)
        foregroundWidgetGridLayout.setRowStretch(1, 1)

        foregroundWidgetGridLayout.setColumnStretch(0, 1)

        foregroundWidgetGridLayout.addWidget(QPushButton("Hello, World!"), 0, 0)
        foregroundWidgetGridLayout.addWidget(QPushButton("Goodbye, World!"), 1, 0)
        foregroundWidget.setLayout(foregroundWidgetGridLayout)

        centralWidget.setLayout(centralWidgetGridLayout)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()