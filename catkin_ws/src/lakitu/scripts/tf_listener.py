#!/usr/bin/env python
import rospy
import tf2_ros
import geometry_msgs.msg

from fiducial_msgs.msg import FiducialTransformArray

# John Millner

def callback(data):
    br = tf.TransformBroadcaster()
    br.sendTransform(,
    

def tfArucoMAVROS():
    #init the node
    rospy.init_node('arucoToPose', anonymous=True)
    
    # bring in the Aruco_detect Transforms messages
    rospy.Subscriber("/fiducial_transforms", FiducialTransformArray, callback)
    
    # broatcast to TF
    # lookup transform between aruco_detect and base_link
    # populate pose message from above's translation/rotation
    # publish pose to aruco_pose

if __name__=='__main__':
	try:
		tfArucoMAVROS()	
	except rospy.ROSInterruptException:
		pass
