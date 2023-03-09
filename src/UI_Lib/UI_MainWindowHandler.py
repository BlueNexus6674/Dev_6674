import sys
import signal
from os import path
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt6 import QtCore, QtGui, QtWidgets

from ROS_Lib import *
import UI_Lib.UI_Main
import UI_Lib.UI_Functions

class MainWindow(QtWidgets.QMainWindow, UI_Lib.UI_Main.Ui_MainWindow, UI_Lib.UI_Functions.UI_Functions, ROS_Lib.ROS_Import.ROS_Import): 
	ROS = []
	DataPath = ""
	
	ROSInit = False
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.actionImport_ROS_Py.triggered.connect(self.Import_ROS_Py)
		self.DataPath = path.abspath(path.join(path.dirname(__file__), '../Data/'))
		self.ROSLabel.setPixmap(QtGui.QPixmap(self.DataPath + "/Images/LEDOff.png"))
		
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
		
		
		

	

