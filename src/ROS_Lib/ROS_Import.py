import sys
from PyQt6 import QtCore, QtGui, QtWidgets

class ROS_Import(object):
	def Import_ROS_Py(self):
		if (self.ROSInit == False):
			sys.path.append("/opt/ros/noetic/lib/python3/dist-packages")
			sys.path.append("/usr/lib/python3/dist-packages")
			
			import rospy
			from std_msgs.msg import String
			self.ROS = [
				rospy, \
				String \
				]
			
			self.ROSInit = True
			self.ROSLabel.setPixmap(QtGui.QPixmap(self.InstallPath + "/Images/ButtonLED/LEDOn.png"))
			print("Import Complete")
			
	
			
		
		
		

	

