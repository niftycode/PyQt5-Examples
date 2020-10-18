#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PyQt5 - Create a main windows using QMainWindow
with a fixed size.
Author: niftycode
Date created: October 18th, 2020
Date modified: -
"""

import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Create a new widget object (window)
        widget = QWidget()
        self.setCentralWidget(widget)
        self.title = 'Qt5-MainWindow with fixed size'
        self.setFixedSize(QSize(800, 600))  # <- fixed size

        # Note: You can also use setMinimumSize() and setMaximumSize()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
