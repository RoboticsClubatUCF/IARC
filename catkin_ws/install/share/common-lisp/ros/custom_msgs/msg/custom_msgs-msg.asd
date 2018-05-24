
(cl:in-package :asdf)

(defsystem "custom_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "StateMachine" :depends-on ("_package_StateMachine"))
    (:file "_package_StateMachine" :depends-on ("_package"))
  ))