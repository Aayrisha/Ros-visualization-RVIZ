#!/usr/bin/python
import rospy
import serial
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from sensor_msgs.msg import Joy
import tf
from std_msgs.msg import Int32
#import MySQLdb
import time
import subprocess
def keys_cb(msg,pub):	
	while(msg.buttons[0]==1):
		ser=serial.Serial('/dev/ttyACM0',9600)
		data=ser.readline()
		pieces=data.split()
	     	act3=pieces[0]
		act1=pieces[1]
		act2=pieces[2]
		print pieces
		hello_str = JointState()
	  	hello_str.header = Header()
                hello_str.header.stamp = rospy.Time.now()
		hello_str.name = ['1','2','3']
	        hello_str.position =[act1,act2,act3]
		hello_str.velocity = [0]
	        hello_str.effort = [0]
		
if __name__ =='__main__':
        rospy.init_node('state_publisher')
	pub = rospy.Publisher('joint_states',JointState,queue_size=100)
        rospy.Subscriber('joy',Joy,keys_cb,pub)
	rospy.spin()






