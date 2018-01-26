#!/usr/bin/env python
# "https://github.com/emlid/mavros-navio-python-example/blob/master/README.md"


''' Code that reads the IMU data from the Pixracer through the use of MAVROS
	ROSTOPIC ECHO will provide list of possible messages to receive
	TODO: write publish command to create message'''

import rospy
from sensor_msgs.msg import Imu, MagneticField
import os
import math

def clear(): #not actually necessary
	os.system( 'clear' )

#stolen from wikipedia, converts quaternions to euler angles (roll, pitch, yaw)
def quaternion_to_euler_angle(w, x, y, z): 

	ysqr = y * y
	
	t0 = +2.0 * (w * x + y * z) 
	t1 = +1.0 - 2.0 * (x * x + ysqr) 
	X = math.degrees(math.atan2(t0, t1))
	
	t2 = +2.0 * (w * y - z * x) 
	t2 = +1.0 if t2 > +1.0 else t2 
	t2 = -1.0 if t2 < -1.0 else t2 
	Y = math.degrees(math.asin(t2))

	t3 = +2.0 * (w * z + x * y) 
	t4 = +1.0 - 2.0 * (ysqr + z * z) 
	Z = math.degrees(math.atan2(t3, t4))
	
	return X, Y, Z	


def callback(data):
	clear()
	#rospy.loginfo(rospy.get_caller_id() + "\nlinear acceleration:\nx: [{}]\ny: [{}]\nz: [{}]".format(data.linear_acceleration.x, data.linear_acceleration.y, data.linear_acceleration.z))
	rospy.loginfo("\nangular velocity:\nx: [{}] \ny: [{}] \nz: [{}]".format(data.angular_velocity.x, data.angular_velocity.y, data.angular_velocity.z))
	print(quaternion_to_euler_angle(data.orientation.w,data.orientation.x,data.orientation.y,data.orientation.z))
	rospy.loginfo("\norientation:\nx: [{}] \ny: [{}] \nz: [{}] \nw: [{}]".format(data.orientation.x,data.orientation.y,data.orientation.z,data.orientation.w))

def heading(data):
	# rospy.loginfo("\nmagnetic field(xyz): \n[{}] \n[{}] \n[{}]".format(data.magnetic_field.x, data.magnetic_field.y, data.magnetic_field.z))
	heading = 180 * math.atan2(data.magnetic_field.y,data.magnetic_field.x)/math.pi
	if heading <0:
		heading += 360
	print heading

def listener():
	rospy.init_node('listener', anonymous=True)
	#the subscribed messages
	rospy.Subscriber("/mavros/imu/data", Imu, callback)
	rospy.Subscriber("/mavros/imu/mag", MagneticField, heading)
	#insert publish command to publish to ROS topic
	rospy.spin()


if __name__=='__main__':
	listener()	