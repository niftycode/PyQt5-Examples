#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PyQt5: 1st window example

Author: niftycode
Date created: March 15th, 2020
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    # Create a window
    window = QWidget()
    window.resize(450, 300)
    window.move(300, 300)
    window.setWindowTitle('Qt5-Window')
    window.show()

    sys.exit(app.exec_())
