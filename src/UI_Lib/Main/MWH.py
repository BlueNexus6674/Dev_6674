import sys
import signal
import os
from os import path as op

from PyQt6 import QtCore, QtGui, QtWidgets

from ROS_Lib import *
import UI_Lib.Main.Main
import UI_Lib.Main.Functions

signal.signal(signal.SIGINT, signal.SIG_DFL)

class MainWindow(QtWidgets.QMainWindow, UI_Lib.Main.Main.Ui_MainWindow, UI_Lib.Main.Functions.UI_Functions, ROS_Lib.ROS_Import.ROS_Import): 
	InstallPath = os.getcwd()
	SrcPath = op.abspath(op.dirname(op.dirname(op.dirname(__file__))))
	
	ROSInit = False
	def __init__(self):
		super().__init__()
		self.SetupUI(self)
		self.actionImport_ROS_Py.triggered.connect(self.Import_ROS_Py)
		self.DataPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Data/'))
		self.ROSLabel.setPixmap(QtGui.QPixmap(self.InstallPath + "/Images/ButtonLED/LEDOff.png"))
		
	def SetupUI(self, MainWindow):
		super().setupUi(MainWindow)
	
	def yesclick(self):
		if (self.ROSInit == True):
			rospy = self.ROS[0]
			String = self.ROS[1]
			pub = rospy.Publisher('chatter', String, queue_size=10)
			rospy.init_node('talker', anonymous=True)
			hello_str = "hello world %s" % rospy.get_time()
			rospy.loginfo(hello_str)
			pub.publish(hello_str)
		else:
			print("ROS Not Imported")
		
		
		

	

