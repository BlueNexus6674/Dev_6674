#!/usr/bin/env python3



#ROS Imports
from __future__ import division
from xml.etree.ElementTree import ElementTree
from xmlrpc.server import SimpleXMLRPCServer

import xml.dom.minidom as dom
import logging.config
import yaml
import multiprocessing

# Core Imports
import sys
import signal

# Custom Imports
from PyQt6 import QtCore, QtGui, QtWidgets
from UI_Lib import *
from ROS_Lib import *


signal.signal(signal.SIGINT, signal.SIG_DFL)

def Main():
	# Main Window Init
	App = QtWidgets.QApplication(sys.argv) 			# Creates the App
	MainWindow = UI_Lib.UI_MainWindowHandler.MainWindow()	# Main Window
	MainWindow.show()						# Shows the UI
	sys.exit(App.exec())						# Executes the App

if __name__ == '__main__':
	Main()
