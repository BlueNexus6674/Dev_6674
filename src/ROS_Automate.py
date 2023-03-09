#!/usr/bin/env python3

# Core Imports
import sys
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Custom Imports
from PyQt6 import QtCore, QtGui, QtWidgets
from UI_Lib import *

def Main():
	# Main Window Init
	App = QtWidgets.QApplication(sys.argv) 			# Creates the App
	MainWindow = UI_Lib.UI_MainWindowHandler.MainWindow()	# Main Window
	MainWindow.show()						# Shows the UI
	sys.exit(App.exec())						# Executes the App

if __name__ == '__main__':
	Main()
