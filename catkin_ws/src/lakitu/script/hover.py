#!/usr/bin/env python

import rospy, mavros
import math
from mavros_msgs.srv import CommandBool, SetMode
from mavros_msgs.msg import State
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped, TwistStamped
from custom_msgs.msg import StateMachine

hover_state = None
current_state = None
current_pos = None

def callback(data):
	
	global hover_state
	hover_state = data.hover
	# print(str(hover_state))

def getCurrentState(data):

	global current_state
	current_state = data

def getCurrentPosition(data):

	global current_pos
	current_pos = data

if __name__=='__main__':

	rospy.init_node('hover_node', anonymous=True)

	rospy.Subscriber("/state_machine/state", StateMachine, callback)
	rospy.Subscriber("/mavros/state", State, getCurrentState)
	rospy.Subscriber('/mavros/local_position/odom', Odometry, getCurrentPosition)

	setModeSrv = rospy.ServiceProxy("/mavros/set_mode", SetMode) #http://wiki.ros.org/mavros/CustomModes

	#msgs sent at 60hz
	rate = rospy.Rate(10)

	#creating pose msg
	pose = PoseStamped()
	pose.pose.position.x = 0
	pose.pose.position.y = 0
	pose.pose.position.z = 0

	#StateMachine msg that will switch Lakitu to 'takeoff' state
	state = StateMachine()
	state.preflight = False
	state.takeoff = False
	state.flight = True
	state.hover = False
	state.land = False
	state.emergency = False

	# last_request = rospy.Time.now()

	#main loop of program
	while not rospy.is_shutdown():

		if(hover_state is None):
			# print('what the fuck')
			continue
		if(current_state is None):
			continue
		if(current_pos is None):
			continue	

		if(hover_state):
			setModeSrv(0, "AUTO.LOITER") #FAILS DUE TO RC FAILSAFE

		rate.sleep()		