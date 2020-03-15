#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Qt5 QMainWindow
Create a main window using a class
Author: niftycode
Date created: March 15th, 2020
"""

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Create a new widget object (window)
        widget = QWidget()
        self.setCentralWidget(widget)
        self.title = 'Qt5-MainWindow'
        self.left = 300
        self.top = 300
        self.width = 450
        self.height = 300
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyle('Windows')  # Fusion (Linux), Macintosh (macOS)
    window = MainWindow()
    sys.exit(app.exec_())
