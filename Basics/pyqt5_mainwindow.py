#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Qt5 QMainWindow

Author: niftycode
Date created: March 15th, 2020
"""

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication)


class MainWindow(QMainWindow):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyle('Windows')  # Fusion, Macintosh
    window = MainWindow()
    sys.exit(app.exec_())
