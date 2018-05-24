#!/usr/bin/env python

import rospy, mavros
import math, numpy
from mavros_msgs.srv import CommandBool, SetMode
from mavros_msgs.msg import State, RCIn
from geometry_msgs.msg import PoseStamped, TwistStamped
from custom_msgs.msg import StateMachine

rcNum = None

def callback(data):

	global rcNum
	rcNum = data.channels[6]

if __name__=='__main__':

	rospy.init_node("init_node", anonymous=True)
	rospy.Subscriber("/mavros/rc/in", RCIn, callback)
	init_state_pub = rospy.Publisher('/state_machine/state', StateMachine, queue_size=100, latch=True)

	state = StateMachine()
	state.preflight = True
	state.takeoff = False
	state.flight = False
	state.hover = False
	state.land = False
	state.emergency = False

	rate = rospy.Rate(60)	

	while not rospy.is_shutdown():
		
		if rcNum == 2113:
                    	init_state_pub.publish(state)
		else:
			print('fuck yourself')
			continue
        	rate.sleep()
