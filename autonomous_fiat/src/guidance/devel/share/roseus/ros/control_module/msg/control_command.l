;; Auto-generated. Do not edit!


(when (boundp 'control_module::control_command)
  (if (not (find-package "CONTROL_MODULE"))
    (make-package "CONTROL_MODULE"))
  (shadow 'control_command (find-package "CONTROL_MODULE")))
(unless (find-package "CONTROL_MODULE::CONTROL_COMMAND")
  (make-package "CONTROL_MODULE::CONTROL_COMMAND"))

(in-package "ROS")
;;//! \htmlinclude control_command.msg.html


(defclass control_module::control_command
  :super ros::object
  :slots (_throttle _steering_angle ))

(defmethod control_module::control_command
  (:init
   (&key
    ((:throttle __throttle) 0.0)
    ((:steering_angle __steering_angle) 0.0)
    )
   (send-super :init)
   (setq _throttle (float __throttle))
   (setq _steering_angle (float __steering_angle))
   self)
  (:throttle
   (&optional __throttle)
   (if __throttle (setq _throttle __throttle)) _throttle)
  (:steering_angle
   (&optional __steering_angle)
   (if __steering_angle (setq _steering_angle __steering_angle)) _steering_angle)
  (:serialization-length
   ()
   (+
    ;; float64 _throttle
    8
    ;; float64 _steering_angle
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _throttle
       (sys::poke _throttle (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _steering_angle
       (sys::poke _steering_angle (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _throttle
     (setq _throttle (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _steering_angle
     (setq _steering_angle (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get control_module::control_command :md5sum-) "9f3b540e5265853adbd53f61d05b89c6")
(setf (get control_module::control_command :datatype-) "control_module/control_command")
(setf (get control_module::control_command :definition-)
      "float64 throttle          # throttle pedal, 1->full acceleration, -1->full brake (adimensional)
float64 steering_angle    # wheels steering angle                                (rad)
")



(provide :control_module/control_command "9f3b540e5265853adbd53f61d05b89c6")


