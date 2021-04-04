# -*- coding: utf-8 -*-
# contactbook/main.py

"""This module provides Contacts application logic."""

import sys

from PyQt5.QtWidgets import QApplication
from .database import createConnection
from .views import Window

def main():
    # Create the application
    app = QApplication(sys.argv)
    # Connect to database
    if not createConnection("contacts.sqlite"):
        sys.exit(1)
    # Create the main window
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec())