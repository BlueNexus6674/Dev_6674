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
import os
import signal

# Custom Imports
from PyQt6 import QtCore, QtGui, QtWidgets

import UI_Lib.Main.MWH
import UI_Lib.Install.MWH

signal.signal(signal.SIGINT, signal.SIG_DFL)

def Main():
	# Check if App is installed (i.e. does config exist)
	print(os.getcwd())
	ConfigPath = (os.getcwd() + "/Config/")
	ConfigFilePath = (ConfigPath + "/Install.txt")
	print(ConfigPath)
	try:
		ConfigFile = open(ConfigFilePath, "r")
	except:
		print("Debug: Install Config File Does Not Exist")

		# Start GUI
		App = QtWidgets.QApplication(sys.argv) 			# Creates the App
		MainWindow = UI_Lib.Install.MWH.MainWindow()			# Main Window
		MainWindow.show()						# Shows the UI
		sys.exit(App.exec())						# Executes the App

	else:
		print("Debug: Install Config File Exists")
		ConfigFile.close()
		
		# Main Window Init
		App = QtWidgets.QApplication(sys.argv) 			# Creates the App
		MainWindow = UI_Lib.Main.MWH.MainWindow()			# Main Window
		MainWindow.show()						# Shows the UI
		sys.exit(App.exec())						# Executes the App
		
							

if __name__ == '__main__':
	Main()
	
	
# App
# Config
# Data
