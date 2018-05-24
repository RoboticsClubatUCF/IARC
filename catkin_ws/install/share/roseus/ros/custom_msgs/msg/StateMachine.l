;; Auto-generated. Do not edit!


(when (boundp 'custom_msgs::StateMachine)
  (if (not (find-package "CUSTOM_MSGS"))
    (make-package "CUSTOM_MSGS"))
  (shadow 'StateMachine (find-package "CUSTOM_MSGS")))
(unless (find-package "CUSTOM_MSGS::STATEMACHINE")
  (make-package "CUSTOM_MSGS::STATEMACHINE"))

(in-package "ROS")
;;//! \htmlinclude StateMachine.msg.html


(defclass custom_msgs::StateMachine
  :super ros::object
  :slots (_preflight _takeoff _flight _hover _land _emergency ))

(defmethod custom_msgs::StateMachine
  (:init
   (&key
    ((:preflight __preflight) nil)
    ((:takeoff __takeoff) nil)
    ((:flight __flight) nil)
    ((:hover __hover) nil)
    ((:land __land) nil)
    ((:emergency __emergency) nil)
    )
   (send-super :init)
   (setq _preflight __preflight)
   (setq _takeoff __takeoff)
   (setq _flight __flight)
   (setq _hover __hover)
   (setq _land __land)
   (setq _emergency __emergency)
   self)
  (:preflight
   (&optional __preflight)
   (if __preflight (setq _preflight __preflight)) _preflight)
  (:takeoff
   (&optional __takeoff)
   (if __takeoff (setq _takeoff __takeoff)) _takeoff)
  (:flight
   (&optional __flight)
   (if __flight (setq _flight __flight)) _flight)
  (:hover
   (&optional __hover)
   (if __hover (setq _hover __hover)) _hover)
  (:land
   (&optional __land)
   (if __land (setq _land __land)) _land)
  (:emergency
   (&optional __emergency)
   (if __emergency (setq _emergency __emergency)) _emergency)
  (:serialization-length
   ()
   (+
    ;; bool _preflight
    1
    ;; bool _takeoff
    1
    ;; bool _flight
    1
    ;; bool _hover
    1
    ;; bool _land
    1
    ;; bool _emergency
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _preflight
       (if _preflight (write-byte -1 s) (write-byte 0 s))
     ;; bool _takeoff
       (if _takeoff (write-byte -1 s) (write-byte 0 s))
     ;; bool _flight
       (if _flight (write-byte -1 s) (write-byte 0 s))
     ;; bool _hover
       (if _hover (write-byte -1 s) (write-byte 0 s))
     ;; bool _land
       (if _land (write-byte -1 s) (write-byte 0 s))
     ;; bool _emergency
       (if _emergency (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _preflight
     (setq _preflight (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _takeoff
     (setq _takeoff (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _flight
     (setq _flight (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _hover
     (setq _hover (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _land
     (setq _land (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _emergency
     (setq _emergency (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get custom_msgs::StateMachine :md5sum-) "3f8a4c584aa1c1f432d46d2dd0cd69f1")
(setf (get custom_msgs::StateMachine :datatype-) "custom_msgs/StateMachine")
(setf (get custom_msgs::StateMachine :definition-)
      "bool preflight
bool takeoff
bool flight
bool hover
bool land
bool emergency

")



(provide :custom_msgs/StateMachine "3f8a4c584aa1c1f432d46d2dd0cd69f1")


