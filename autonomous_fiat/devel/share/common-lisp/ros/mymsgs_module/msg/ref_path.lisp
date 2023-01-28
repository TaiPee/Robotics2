; Auto-generated. Do not edit!


(cl:in-package mymsgs_module-msg)


;//! \htmlinclude ref_path.msg.html

(cl:defclass <ref_path> (roslisp-msg-protocol:ros-message)
  ((points
    :reader points
    :initarg :points
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass ref_path (<ref_path>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ref_path>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ref_path)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mymsgs_module-msg:<ref_path> is deprecated: use mymsgs_module-msg:ref_path instead.")))

(cl:ensure-generic-function 'points-val :lambda-list '(m))
(cl:defmethod points-val ((m <ref_path>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mymsgs_module-msg:points-val is deprecated.  Use mymsgs_module-msg:points instead.")
  (points m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ref_path>) ostream)
  "Serializes a message object of type '<ref_path>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'points))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'points))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ref_path>) istream)
  "Deserializes a message object of type '<ref_path>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'points) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'points)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ref_path>)))
  "Returns string type for a message object of type '<ref_path>"
  "mymsgs_module/ref_path")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ref_path)))
  "Returns string type for a message object of type 'ref_path"
  "mymsgs_module/ref_path")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ref_path>)))
  "Returns md5sum for a message object of type '<ref_path>"
  "93c76054c676123f8fabd76bcbdae971")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ref_path)))
  "Returns md5sum for a message object of type 'ref_path"
  "93c76054c676123f8fabd76bcbdae971")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ref_path>)))
  "Returns full string definition for message of type '<ref_path>"
  (cl:format cl:nil "float32[] points~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ref_path)))
  "Returns full string definition for message of type 'ref_path"
  (cl:format cl:nil "float32[] points~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ref_path>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'points) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ref_path>))
  "Converts a ROS message object to a list"
  (cl:list 'ref_path
    (cl:cons ':points (points msg))
))
