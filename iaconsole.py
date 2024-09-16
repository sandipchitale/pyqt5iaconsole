# PyQt5 introduction
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QMouseEvent
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QGridLayout, QVBoxLayout, QSizePolicy,
                             QToolBar, QPushButton)


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
        self.backgroundImage = QPixmap("assets/iaconsole-bg.png")
        self.setGeometry(500, 100,
                         self.backgroundImage.size().width(), self.backgroundImage.size().height())
        self.setWindowOpacity(0.0)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint)

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
        # add in cell 0,0 to backgroundLabel
        centralWidgetGridLayout.addWidget(foregroundWidget, 0, 0)

        foregroundWidget.setMouseTracking(True)
        foregroundWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        foregroundWidgetLayout = QVBoxLayout()
        foregroundWidgetLayout.setContentsMargins(20, 60, 19, 50)
        foregroundWidgetLayout.setSpacing(0)

        primaryToolbar = QToolBar()
        foregroundWidgetLayout.addWidget(primaryToolbar)
        foregroundWidgetLayout.setStretch(0, 0)

        primaryToolbarLayout = primaryToolbar.layout()
        primaryToolbarLayout.setSpacing(4)

        foregroundWidgetLayout.addStretch(1)

        foregroundWidgetLayout.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.exitButton.setStyleSheet("border-radius: 14px; border: 1 solid #bbb; padding: 6px 10px;")
        # noinspection PyUnresolvedReferences
        self.exitButton.clicked.connect(lambda: sys.exit(0))
        primaryToolbar.addWidget(self.exitButton)

        foregroundWidget.setLayout(foregroundWidgetLayout)

        centralWidget.setLayout(centralWidgetGridLayout)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
