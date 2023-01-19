; Auto-generated. Do not edit!


(cl:in-package mymsgs_module-msg)


;//! \htmlinclude control_command.msg.html

(cl:defclass <control_command> (roslisp-msg-protocol:ros-message)
  ((velocity
    :reader velocity
    :initarg :velocity
    :type cl:float
    :initform 0.0)
   (steering
    :reader steering
    :initarg :steering
    :type cl:float
    :initform 0.0))
)

(cl:defclass control_command (<control_command>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <control_command>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'control_command)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mymsgs_module-msg:<control_command> is deprecated: use mymsgs_module-msg:control_command instead.")))

(cl:ensure-generic-function 'velocity-val :lambda-list '(m))
(cl:defmethod velocity-val ((m <control_command>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mymsgs_module-msg:velocity-val is deprecated.  Use mymsgs_module-msg:velocity instead.")
  (velocity m))

(cl:ensure-generic-function 'steering-val :lambda-list '(m))
(cl:defmethod steering-val ((m <control_command>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mymsgs_module-msg:steering-val is deprecated.  Use mymsgs_module-msg:steering instead.")
  (steering m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <control_command>) ostream)
  "Serializes a message object of type '<control_command>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'velocity))))
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
    (cl:setf (cl:slot-value msg 'velocity) (roslisp-utils:decode-double-float-bits bits)))
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<control_command>)))
  "Returns string type for a message object of type '<control_command>"
  "mymsgs_module/control_command")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'control_command)))
  "Returns string type for a message object of type 'control_command"
  "mymsgs_module/control_command")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<control_command>)))
  "Returns md5sum for a message object of type '<control_command>"
  "2cccf116fd404cf82580c85a4b8c480d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'control_command)))
  "Returns md5sum for a message object of type 'control_command"
  "2cccf116fd404cf82580c85a4b8c480d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<control_command>)))
  "Returns full string definition for message of type '<control_command>"
  (cl:format cl:nil "float64 velocity          # desired velocity        (m/s)~%float64 steering    # wheels steering angle   (rad)~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'control_command)))
  "Returns full string definition for message of type 'control_command"
  (cl:format cl:nil "float64 velocity          # desired velocity        (m/s)~%float64 steering    # wheels steering angle   (rad)~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <control_command>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <control_command>))
  "Converts a ROS message object to a list"
  (cl:list 'control_command
    (cl:cons ':velocity (velocity msg))
    (cl:cons ':steering (steering msg))
))
