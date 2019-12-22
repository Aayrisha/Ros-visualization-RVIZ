#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import tf
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist

def callback(msg,pub):	
		
	if(msg.Buttons[0]==1):
		hello_str = JointState()
		hello_str.header = Header()
		                                          
		hello_str.header.stamp = rospy.Time.now()
		hello_str.name = ['1','2','3']
		
		hello_str.position =[msg.linear.x,msg.linear.y,msg.linear.z]
		#hello_str.position =(msg.linear.y)
		#hello_str.position = (msg.linear.z)
		hello_str.velocity = [0]
		hello_str.effort = [0]
		pub.publish(hello_str)
		
		print hello_str.position
#print msg
	

	
if __name__ == '__main__':
	rospy.init_node('state_publisher')
	pub = rospy.Publisher('joint_states', JointState, queue_size=100)
	sub = rospy.Subscriber('feedback', Twist, callback,pub)   
	
	#rate = rospy.Rate(1)
	rospy.spin()

