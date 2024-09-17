# PyQt5 introduction
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QMouseEvent
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QGridLayout, QVBoxLayout, QSizePolicy,
                             QPushButton, QHBoxLayout)


class ForegroundWidget(QWidget):
    def __init__(self, mainWindow: QMainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.dragging = False
        self.prevX = -1
        self.prevY = -1

    def mousePressEvent(self, e: QMouseEvent):
        super().mousePressEvent(e)
        if e.button() == Qt.LeftButton:
            self.dragging = True
            self.prevX = e.globalX()
            self.prevY = e.globalY()

    def mouseMoveEvent(self, e: QMouseEvent):
        super().mouseMoveEvent(e)
        if self.dragging:
            deltaX = e.globalX() - self.prevX
            deltaY = e.globalY() - self.prevY
            self.mainWindow.move(self.mainWindow.x() + deltaX, self.mainWindow.y() + deltaY)
            self.prevX = e.globalX()
            self.prevY = e.globalY()

    def mouseReleaseEvent(self, e: QMouseEvent):
        super().mouseReleaseEvent(e)
        if e.button() == Qt.LeftButton:
            self.dragging = False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("iaconsole")

        # preload background image pixmap
        self.backgroundImage = QPixmap("assets/iaconsole-tablet.png")
        self.setGeometry(300, 100, self.backgroundImage.size().width(), self.backgroundImage.size().height())
        self.setWindowOpacity(0.0)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.exitButton = QPushButton("⨉")

        self.initUI()

    def initUI(self):
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        centralWidgetGridLayout = QGridLayout()

        # Background label
        backgroundLabel = QLabel("iaconsole", self)
        backgroundLabel.setPixmap(self.backgroundImage)
        # add in cell 0,0
        centralWidgetGridLayout.addWidget(backgroundLabel, 0, 0)

        # Main Panel
        foregroundWidget = ForegroundWidget(self)
        foregroundWidget.setMouseTracking(True)
        foregroundWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        foregroundWidgetLayout = QVBoxLayout()
        foregroundWidget.setLayout(foregroundWidgetLayout)

        foregroundWidgetLayout.setContentsMargins(20, 60, 20, 50)
        foregroundWidgetLayout.setSpacing(0)

        primaryToolbar = QWidget()

        primaryToolbarLayout = QHBoxLayout()
        primaryToolbar.setLayout(primaryToolbarLayout)

        primaryToolbarLayout.setSpacing(4)

        # Left stretch
        primaryToolbarLayout.addStretch()

        self.exitButton.setStyleSheet("border-radius: 14px; border: 1 solid #bbb; padding: 6px 10px;")
        # noinspection PyUnresolvedReferences
        self.exitButton.clicked.connect(lambda: sys.exit(0))
        primaryToolbarLayout.addWidget(self.exitButton)

        foregroundWidgetLayout.addWidget(primaryToolbar)

        foregroundWidgetLayout.addStretch(1)

        # add in cell 0,0 to backgroundLabel
        centralWidgetGridLayout.addWidget(foregroundWidget, 0, 0)

        centralWidget.setLayout(centralWidgetGridLayout)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
