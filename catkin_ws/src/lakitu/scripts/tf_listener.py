#!/usr/bin/env python
import rospy
import tf2_ros
import tf
from geometry_msgs.msg import PoseStamped

from fiducial_msgs.msg import FiducialTransformArray

# John Millner

def callback(data):
    # broatcast to TF
    br = tf.TransformBroadcaster()
    br.sendTransform(   data.transforms[0].translation, 
                        data.transforms[0].rotation, 
                        data.header.stamp, 
                        "camera", 
                        "fiducial")
    

def tfArucoMAVROS():
    #init the node
    rospy.init_node('arucoToPose', anonymous=True)
    
    # init the publisher
    pub = rospy.Publisher('poseOfAruco', PoseStamped, queue_size=10)
    
    #init the tf listener
    listener = tf.TransformListener("fiducial", "base_link", rospy.Time)
     
    # bring in the Aruco_detect Transforms messages
    rospy.Subscriber("/fiducial_transforms", FiducialTransformArray, callback)
    
    # lookup transform between aruco_detect and base_link
    (trans, rot) = listener.lookupTransform( "fiducial", "base_link", rospy.Time ) 
     
    # populate pose message from above's translation/rotation
    msg = PoseStamped()
    msg.header.seq = i
    msg.header.stamp = rospy.Time
    msg.header.frame_id = 0
    msg.pose.point = trans
    msg.pose.orientation = rot
    
    # publish pose to aruco_pose
    pub.publish(msg)
    
    rospy.spin()

if __name__=='__main__':
	try:
		tfArucoMAVROS()	
	except rospy.ROSInterruptException:
		pass
