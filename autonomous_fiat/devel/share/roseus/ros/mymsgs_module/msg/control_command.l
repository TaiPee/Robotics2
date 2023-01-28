;; Auto-generated. Do not edit!


(when (boundp 'mymsgs_module::control_command)
  (if (not (find-package "MYMSGS_MODULE"))
    (make-package "MYMSGS_MODULE"))
  (shadow 'control_command (find-package "MYMSGS_MODULE")))
(unless (find-package "MYMSGS_MODULE::CONTROL_COMMAND")
  (make-package "MYMSGS_MODULE::CONTROL_COMMAND"))

(in-package "ROS")
;;//! \htmlinclude control_command.msg.html


(defclass mymsgs_module::control_command
  :super ros::object
  :slots (_velocity _steering ))

(defmethod mymsgs_module::control_command
  (:init
   (&key
    ((:velocity __velocity) 0.0)
    ((:steering __steering) 0.0)
    )
   (send-super :init)
   (setq _velocity (float __velocity))
   (setq _steering (float __steering))
   self)
  (:velocity
   (&optional __velocity)
   (if __velocity (setq _velocity __velocity)) _velocity)
  (:steering
   (&optional __steering)
   (if __steering (setq _steering __steering)) _steering)
  (:serialization-length
   ()
   (+
    ;; float64 _velocity
    8
    ;; float64 _steering
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _velocity
       (sys::poke _velocity (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _steering
       (sys::poke _steering (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _velocity
     (setq _velocity (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _steering
     (setq _steering (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get mymsgs_module::control_command :md5sum-) "2cccf116fd404cf82580c85a4b8c480d")
(setf (get mymsgs_module::control_command :datatype-) "mymsgs_module/control_command")
(setf (get mymsgs_module::control_command :definition-)
      "float64 velocity          # desired velocity        (m/s)
float64 steering    # wheels steering angle   (rad)
")



(provide :mymsgs_module/control_command "2cccf116fd404cf82580c85a4b8c480d")


