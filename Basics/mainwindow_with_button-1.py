#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PyQt5 - Create a main windows using QMainWindow
with a button widget (QPushButton).
1st example

Author: niftycode
Date created: October 18th, 2020
"""

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Create a new widget object (button)
        button = QPushButton("Click me!")
        self.setCentralWidget(button)
        self.title = 'Qt5-MainWindow with button'
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
