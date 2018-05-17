#!/usr/bin/env python

import rospy, mavros
import math
from mavros_msgs.srv import CommandBool, SetMode
from mavros_msgs.msg import State
from geometry_msgs.msg import PoseStamped, TwistStamped
#from custom_msgs.msg import StateMachine


if __name__=='__main__':

	rospy.init_node("init_node", anonymous=True)
	init_state_pub = rospy.Publisher('/state_machine/state', StateMachine, queue_size=100, latch=True)

	state = StateMachine()
	state.preflight = True
	state.takeoff = False
	state.flight = False
	state.hover = False
	state.land = False
	state.emergency = False

	init_state_pub.publish(state)

	while not rospy.is_shutdown():
		rospy.spin()
