; Auto-generated. Do not edit!


(cl:in-package custom_msgs-msg)


;//! \htmlinclude StateMachine.msg.html

(cl:defclass <StateMachine> (roslisp-msg-protocol:ros-message)
  ((preflight
    :reader preflight
    :initarg :preflight
    :type cl:boolean
    :initform cl:nil)
   (takeoff
    :reader takeoff
    :initarg :takeoff
    :type cl:boolean
    :initform cl:nil)
   (flight
    :reader flight
    :initarg :flight
    :type cl:boolean
    :initform cl:nil)
   (hover
    :reader hover
    :initarg :hover
    :type cl:boolean
    :initform cl:nil)
   (land
    :reader land
    :initarg :land
    :type cl:boolean
    :initform cl:nil)
   (emergency
    :reader emergency
    :initarg :emergency
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass StateMachine (<StateMachine>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StateMachine>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StateMachine)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name custom_msgs-msg:<StateMachine> is deprecated: use custom_msgs-msg:StateMachine instead.")))

(cl:ensure-generic-function 'preflight-val :lambda-list '(m))
(cl:defmethod preflight-val ((m <StateMachine>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msgs-msg:preflight-val is deprecated.  Use custom_msgs-msg:preflight instead.")
  (preflight m))

(cl:ensure-generic-function 'takeoff-val :lambda-list '(m))
(cl:defmethod takeoff-val ((m <StateMachine>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msgs-msg:takeoff-val is deprecated.  Use custom_msgs-msg:takeoff instead.")
  (takeoff m))

(cl:ensure-generic-function 'flight-val :lambda-list '(m))
(cl:defmethod flight-val ((m <StateMachine>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msgs-msg:flight-val is deprecated.  Use custom_msgs-msg:flight instead.")
  (flight m))

(cl:ensure-generic-function 'hover-val :lambda-list '(m))
(cl:defmethod hover-val ((m <StateMachine>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msgs-msg:hover-val is deprecated.  Use custom_msgs-msg:hover instead.")
  (hover m))

(cl:ensure-generic-function 'land-val :lambda-list '(m))
(cl:defmethod land-val ((m <StateMachine>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msgs-msg:land-val is deprecated.  Use custom_msgs-msg:land instead.")
  (land m))

(cl:ensure-generic-function 'emergency-val :lambda-list '(m))
(cl:defmethod emergency-val ((m <StateMachine>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msgs-msg:emergency-val is deprecated.  Use custom_msgs-msg:emergency instead.")
  (emergency m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StateMachine>) ostream)
  "Serializes a message object of type '<StateMachine>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'preflight) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'takeoff) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'flight) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'hover) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'land) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'emergency) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StateMachine>) istream)
  "Deserializes a message object of type '<StateMachine>"
    (cl:setf (cl:slot-value msg 'preflight) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'takeoff) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'flight) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'hover) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'land) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'emergency) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StateMachine>)))
  "Returns string type for a message object of type '<StateMachine>"
  "custom_msgs/StateMachine")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StateMachine)))
  "Returns string type for a message object of type 'StateMachine"
  "custom_msgs/StateMachine")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StateMachine>)))
  "Returns md5sum for a message object of type '<StateMachine>"
  "3f8a4c584aa1c1f432d46d2dd0cd69f1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StateMachine)))
  "Returns md5sum for a message object of type 'StateMachine"
  "3f8a4c584aa1c1f432d46d2dd0cd69f1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StateMachine>)))
  "Returns full string definition for message of type '<StateMachine>"
  (cl:format cl:nil "bool preflight~%bool takeoff~%bool flight~%bool hover~%bool land~%bool emergency~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StateMachine)))
  "Returns full string definition for message of type 'StateMachine"
  (cl:format cl:nil "bool preflight~%bool takeoff~%bool flight~%bool hover~%bool land~%bool emergency~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StateMachine>))
  (cl:+ 0
     1
     1
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StateMachine>))
  "Converts a ROS message object to a list"
  (cl:list 'StateMachine
    (cl:cons ':preflight (preflight msg))
    (cl:cons ':takeoff (takeoff msg))
    (cl:cons ':flight (flight msg))
    (cl:cons ':hover (hover msg))
    (cl:cons ':land (land msg))
    (cl:cons ':emergency (emergency msg))
))
