#!/usr/bin/env python

import rospy, mavros
import math
from mavros_msgs.srv import CommandBool, SetMode
from mavros_msgs.msg import State, RCIn
from geometry_msgs.msg import PoseStamped, TwistStamped
from custom_msgs.msg import StateMachine


''' init state listens for rc start switch, then publishes the first StateMachine msg'''

rcNum = None

def flightCallback(data):

	flight_pub.publish(data)


def callback(data):

	global rcNum
	rcNum = data.channels[6]

if __name__=='__main__':

	rospy.init_node("init_node", anonymous=True)

	rospy.Subscriber("/mavros/rc/in", RCIn, callback) #subscribe to mavros topic for RC Data
	rospy.Subscriber("/lakitu/flight_target", PoseStamped, flightCallback)
	
	init_state_pub = rospy.Publisher('/state_machine/state', StateMachine, queue_size=100, latch=True)
	flight_pub = rospy.Publisher('/mavros/setpoint_position/local', PoseStamped, queue_size=100, latch=True)

	state = StateMachine() #should switch state to preflight when RC switch flipped
	state.preflight = True
	state.takeoff = False
	state.flight = False
	state.hover = False
	state.land = False
	state.emergency = False

	rate = rospy.Rate(60) #refreshes at 60 Hz	

	flag = True #to stop constant publishing of preflight state

	while not rospy.is_shutdown():
		
		if rcNum == 2113 and flag: #listens for RC switch, publishes state ONCE
			init_state_pub.publish(state)
			flag = False

		rate.sleep()
