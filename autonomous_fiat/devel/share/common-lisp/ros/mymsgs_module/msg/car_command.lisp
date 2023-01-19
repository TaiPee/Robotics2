; Auto-generated. Do not edit!


(cl:in-package mymsgs_module-msg)


;//! \htmlinclude car_command.msg.html

(cl:defclass <car_command> (roslisp-msg-protocol:ros-message)
  ((throttle
    :reader throttle
    :initarg :throttle
    :type cl:float
    :initform 0.0)
   (steering
    :reader steering
    :initarg :steering
    :type cl:float
    :initform 0.0))
)

(cl:defclass car_command (<car_command>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <car_command>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'car_command)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mymsgs_module-msg:<car_command> is deprecated: use mymsgs_module-msg:car_command instead.")))

(cl:ensure-generic-function 'throttle-val :lambda-list '(m))
(cl:defmethod throttle-val ((m <car_command>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mymsgs_module-msg:throttle-val is deprecated.  Use mymsgs_module-msg:throttle instead.")
  (throttle m))

(cl:ensure-generic-function 'steering-val :lambda-list '(m))
(cl:defmethod steering-val ((m <car_command>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mymsgs_module-msg:steering-val is deprecated.  Use mymsgs_module-msg:steering instead.")
  (steering m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <car_command>) ostream)
  "Serializes a message object of type '<car_command>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'throttle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'steering))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <car_command>) istream)
  "Deserializes a message object of type '<car_command>"
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
    (cl:setf (cl:slot-value msg 'steering) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<car_command>)))
  "Returns string type for a message object of type '<car_command>"
  "mymsgs_module/car_command")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'car_command)))
  "Returns string type for a message object of type 'car_command"
  "mymsgs_module/car_command")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<car_command>)))
  "Returns md5sum for a message object of type '<car_command>"
  "39f463d271c2ca10c14182802c72c029")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'car_command)))
  "Returns md5sum for a message object of type 'car_command"
  "39f463d271c2ca10c14182802c72c029")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<car_command>)))
  "Returns full string definition for message of type '<car_command>"
  (cl:format cl:nil "float64 throttle          # throttle pedal, 1->full acceleration, -1->full brake (adimensional)~%float64 steering    # wheels steering angle                                (rad)~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'car_command)))
  "Returns full string definition for message of type 'car_command"
  (cl:format cl:nil "float64 throttle          # throttle pedal, 1->full acceleration, -1->full brake (adimensional)~%float64 steering    # wheels steering angle                                (rad)~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <car_command>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <car_command>))
  "Converts a ROS message object to a list"
  (cl:list 'car_command
    (cl:cons ':throttle (throttle msg))
    (cl:cons ':steering (steering msg))
))
