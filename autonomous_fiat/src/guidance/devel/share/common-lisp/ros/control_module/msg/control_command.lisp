; Auto-generated. Do not edit!


(cl:in-package control_module-msg)


;//! \htmlinclude control_command.msg.html

(cl:defclass <control_command> (roslisp-msg-protocol:ros-message)
  ((throttle
    :reader throttle
    :initarg :throttle
    :type cl:float
    :initform 0.0)
   (steering_angle
    :reader steering_angle
    :initarg :steering_angle
    :type cl:float
    :initform 0.0))
)

(cl:defclass control_command (<control_command>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <control_command>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'control_command)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name control_module-msg:<control_command> is deprecated: use control_module-msg:control_command instead.")))

(cl:ensure-generic-function 'throttle-val :lambda-list '(m))
(cl:defmethod throttle-val ((m <control_command>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_module-msg:throttle-val is deprecated.  Use control_module-msg:throttle instead.")
  (throttle m))

(cl:ensure-generic-function 'steering_angle-val :lambda-list '(m))
(cl:defmethod steering_angle-val ((m <control_command>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_module-msg:steering_angle-val is deprecated.  Use control_module-msg:steering_angle instead.")
  (steering_angle m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <control_command>) ostream)
  "Serializes a message object of type '<control_command>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'throttle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'steering_angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <control_command>) istream)
  "Deserializes a message object of type '<control_command>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'throttle) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'steering_angle) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<control_command>)))
  "Returns string type for a message object of type '<control_command>"
  "control_module/control_command")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'control_command)))
  "Returns string type for a message object of type 'control_command"
  "control_module/control_command")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<control_command>)))
  "Returns md5sum for a message object of type '<control_command>"
  "9f3b540e5265853adbd53f61d05b89c6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'control_command)))
  "Returns md5sum for a message object of type 'control_command"
  "9f3b540e5265853adbd53f61d05b89c6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<control_command>)))
  "Returns full string definition for message of type '<control_command>"
  (cl:format cl:nil "float64 throttle          # throttle pedal, 1->full acceleration, -1->full brake (adimensional)~%float64 steering_angle    # wheels steering angle                                (rad)~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'control_command)))
  "Returns full string definition for message of type 'control_command"
  (cl:format cl:nil "float64 throttle          # throttle pedal, 1->full acceleration, -1->full brake (adimensional)~%float64 steering_angle    # wheels steering angle                                (rad)~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <control_command>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <control_command>))
  "Converts a ROS message object to a list"
  (cl:list 'control_command
    (cl:cons ':throttle (throttle msg))
    (cl:cons ':steering_angle (steering_angle msg))
))
