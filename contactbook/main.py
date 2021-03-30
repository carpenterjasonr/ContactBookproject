# -*- coding: utf-8 -*-
# contactbook/main.py

"""This module provides Contacts application logic."""

import sys

from PyQt5.QtWidgets import QApplication

from .views import Window

def main():
    # Create the application
    app = QApplication(sys.argv)
    # Create the main window
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec())