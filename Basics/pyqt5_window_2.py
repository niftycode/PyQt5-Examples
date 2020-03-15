#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PyQt5: 2nd window example
Create a window using a class

Author: niftycode
Date created: March 15th, 2020
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget


class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Qt5-Window'
        self.left = 300
        self.top = 300
        self.width = 450
        self.height = 300
        self.init_ui()

    def init_ui(self):
        # Set basic window layout
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example_window = SimpleApp()
    sys.exit(app.exec_())
