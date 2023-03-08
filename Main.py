#!/usr/bin/env python3

# Dev_6674 Main

# Core Imports
import sys
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Custom Imports
from PyQt5 import QtCore, QtGui, QtWidgets
from UI_Lib import *

def Main():
	# Main Window Init
	App = QtWidgets.QApplication(sys.argv) 	# Creates the App
	MainWindow = QtWidgets.QMainWindow()		# Defines Main Window
	Ui = UI_Main.Ui_MainWindow()			# Set Ui as the Ui of MainWindow
	Ui.setupUi(MainWindow)				# Calls the windows Setup function
	
	MainWindow.show()				# Shows the UI
	
	sys.exit(App.exec_())				# Executes the App


if __name__ == "__main__":
    Main()
    
    
    
