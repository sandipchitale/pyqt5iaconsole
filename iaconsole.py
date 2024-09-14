# PyQt5 introduction
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QMouseEvent
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QGridLayout, QVBoxLayout, QSizePolicy,
                             QToolBox, QToolBar, QHBoxLayout, QPushButton, QComboBox)


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

        # Background label
        backgroundImage = QPixmap("assets/iaconsole-bg.png")
        backgroundLabel = QLabel("iaconsole", self)
        backgroundLabel.setPixmap(backgroundImage)
        # add in cell 0,0
        centralWidgetGridLayout.addWidget(backgroundLabel, 0, 0)

        # Main Panel
        foregroundWidget = ForegroundWidget(self)
        # add in cell 0,0 to backgroundLabel
        centralWidgetGridLayout.addWidget(foregroundWidget, 0, 0)

        foregroundWidget.setMouseTracking(True)
        foregroundWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        foregroundWidgetLayout = QVBoxLayout()
        foregroundWidgetLayout.setContentsMargins(20,60,19,50)
        foregroundWidgetLayout.setSpacing(0)

        primaryToolbar = QToolBar()
        foregroundWidgetLayout.addWidget(primaryToolbar)
        foregroundWidgetLayout.setStretch(0, 0)

        primaryToolbarLayout = primaryToolbar.layout()
        primaryToolbarLayout.setSpacing(4)

        branches = QComboBox()
        branches.setStyleSheet("padding: 3px 8px;")
        branches.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        branches.addItem("Main")
        branches.addItem("24.4")
        primaryToolbar.addWidget(branches)

        downloadButton = QPushButton("V")
        downloadButton.setStyleSheet("padding: 4px 8px;")
        primaryToolbar.addWidget(downloadButton)

        extractButton = QPushButton("_")
        extractButton.setStyleSheet("padding: 4px 8px;")
        primaryToolbar.addWidget(extractButton)

        installButton = QPushButton("I")
        installButton.setStyleSheet("padding: 4px 10px;")
        primaryToolbar.addWidget(installButton)

        exitButton = QPushButton("X")
        exitButton.setStyleSheet("padding: 4px 10px;")
        primaryToolbar.addWidget(exitButton)
        exitButton.clicked.connect(lambda e: sys.exit(0))

        secondaryToolbar = QToolBar()
        foregroundWidgetLayout.addWidget(secondaryToolbar)
        foregroundWidgetLayout.setStretch(1, 0)

        secondaryToolbarLayout = secondaryToolbar.layout()
        secondaryToolbarLayout.setSpacing(4)

        downloadButton = QPushButton("V")
        downloadButton.setStyleSheet("padding: 4px 8px;")
        secondaryToolbar.addWidget(downloadButton)

        extractButton = QPushButton("X")
        extractButton.setStyleSheet("padding: 4px 8px;")
        secondaryToolbar.addWidget(extractButton)

        installButton = QPushButton("I")
        installButton.setStyleSheet("padding: 4px 10px;")
        secondaryToolbar.addWidget(installButton)

        foregroundWidgetLayout.addStretch(1)

        foregroundWidget.setLayout(foregroundWidgetLayout)

        centralWidget.setLayout(centralWidgetGridLayout)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
