#!/usr/bin/env python
# "https://github.com/emlid/mavros-navio-python-example/blob/master/README.md"


''' Code that reads the IMU data from the Pixracer through the use of MAVROS
	ROSTOPIC ECHO will provide list of possible messages to receive
	'''

import rospy
from sensor_msgs.msg import Imu, MagneticField
import os
import math
import tf

def clear(): #not actually necessary
	os.system( 'clear' )

#stolen from wikipedia, converts quaternions to euler angles (roll, pitch, yaw)
def quaternion_to_euler_angle(w, x, y, z): 

	ysqr = y * y
	
	t0 = +2.0 * (w * x + y * z) 
	t1 = +1.0 - 2.0 * (x * x + ysqr) 
	X = math.degrees(math.atan2(t0, t1)) #x=roll
	t2 = +2.0 * (w * y - z * x) 
	t2 = +1.0 if t2 > +1.0 else t2 
	t2 = -1.0 if t2 < -1.0 else t2 
	Y = math.degrees(math.asin(t2)) #y=pitch
	t3 = +2.0 * (w * z + x * y) 
	t4 = +1.0 - 2.0 * (ysqr + z * z) 
	Z = math.degrees(math.atan2(t3, t4))#z=yaw
	
	return X, Y, Z


def callback(data):
	clear()
	#rospy.loginfo(rospy.get_caller_id() + "\nlinear acceleration:\nx: [{}]\ny: [{}]\nz: [{}]".format(data.linear_acceleration.x, data.linear_acceleration.y, data.linear_acceleration.z))
	rospy.loginfo("\nangular velocity:\nx: [{}] \ny: [{}] \nz: [{}]".format(data.angular_velocity.x, data.angular_velocity.y, data.angular_velocity.z))
	print(quaternion_to_euler_angle(data.orientation.w,data.orientation.x,data.orientation.y,data.orientation.z))
	# rospy.loginfo("\norientation:\nx: [{}] \ny: [{}] \nz: [{}] \nw: [{}]".format(data.orientation.x,data.orientation.y,data.orientation.z,data.orientation.w))

def heading(data):
	# rospy.loginfo("\nmagnetic field(xyz): \n[{}] \n[{}] \n[{}]".format(data.magnetic_field.x, data.magnetic_field.y, data.magnetic_field.z))
	heading = 180 * math.atan2(data.magnetic_field.y,data.magnetic_field.x)/math.pi
	if heading <0:
		heading += 360
	print heading

def listener(): #subscribes to the mavros nodes, inits listener and imu_node nodes
	rospy.init_node('listener', anonymous=True)
	
	#the subscribed messages
	rospy.Subscriber("/mavros/imu/data", Imu, callback) #changed to talker_imu from callback
	rospy.Subscriber("/mavros/imu/mag", MagneticField, callback) #changed to talker_mag from callback
	rospy.spin()

def talker_imu(data):
	pub = rospy.Publisher("imu_data", Imu, queue_size=100) 
	rospy.init_node('imu_node', anonymous=True) #moved from within talker_imu
	rate = rospy.Rate(10)

	imu_msg = Imu()
	imu_msg.header.stamp = rospy.Time.now()
	imu_msg.header.frame_id = ""




	while not rospy.is_shutdown():
		pub.publish(data)
		rate.sleep()
		
def talker_mag(data): #not sure if magenetic heading is even needed
	pass		

def tf_broadcast(): #static broadcaster that tells baselink where IMU is
	pass

if __name__=='__main__':
	try:
		listener()	
	except rospy.ROSInterruptException:
		pass