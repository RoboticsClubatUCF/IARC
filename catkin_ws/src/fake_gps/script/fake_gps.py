#!/usr/bin/env python

import rospy
import math
from nav_msgs.msg import Odometry

odomPub = rospy.Publisher('/odom', Odometry, queue_size=10)
rospy.init_node('fake_gps', anonymous=True)

initTime = rospy.get_time()
rate = rospy.Rate(50) # hz

odom = Odometry()

odom.header.frame_id = '/base_link'
odom.pose.pose.position.x = 0.1
odom.pose.pose.position.y = 0.2
odom.pose.pose.position.z = 0.3

odom.pose.pose.orientation.x = 0.4
odom.pose.pose.orientation.y = 0.5
odom.pose.pose.orientation.z = 0.6
odom.pose.pose.orientation.w = 0.7

odom.twist.twist.linear.x = 0.8
odom.twist.twist.linear.y = 0.9
odom.twist.twist.linear.z = 1.0

odom.twist.twist.angular.x = 1.1
odom.twist.twist.angular.y = 1.2
odom.twist.twist.angular.z = 1.3

covar = [1.0,0,0,0,0,0,
	0,1.0,0,0,0,0,
	0,0,1.0,0,0,0,
	0,0,0,9999,0,0,
	0,0,0,0,9999,0,
	0,0,0,0,0,9999]
odom.pose.covariance = covar
odom.twist.covariance = covar

while not rospy.is_shutdown():
	odom.header.stamp = rospy.Time.now()
	odomPub.publish(odom)
	rate.sleep()
