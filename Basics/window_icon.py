#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QMainWindow with window icon (Windows and Linux)
Author: niftycode
Date created: March 15th, 2020
"""

import sys
from PyQt5.QtGui import QIcon  # <- Don't forget to import this module!
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        self.title = 'App with window icon'

        # Set app icon
        self.window_icon = 'img/window_icon.png'

        self.left = 300
        self.top = 300
        self.width = 500
        self.height = 200

        self.init_ui()

    def init_ui(self):

        # Set basic window layout
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.window_icon))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    window = MainWindow()
    sys.exit(app.exec_())
