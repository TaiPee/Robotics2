;; Auto-generated. Do not edit!


(when (boundp 'mymsgs_module::car_command)
  (if (not (find-package "MYMSGS_MODULE"))
    (make-package "MYMSGS_MODULE"))
  (shadow 'car_command (find-package "MYMSGS_MODULE")))
(unless (find-package "MYMSGS_MODULE::CAR_COMMAND")
  (make-package "MYMSGS_MODULE::CAR_COMMAND"))

(in-package "ROS")
;;//! \htmlinclude car_command.msg.html


(defclass mymsgs_module::car_command
  :super ros::object
  :slots (_throttle _steering ))

(defmethod mymsgs_module::car_command
  (:init
   (&key
    ((:throttle __throttle) 0.0)
    ((:steering __steering) 0.0)
    )
   (send-super :init)
   (setq _throttle (float __throttle))
   (setq _steering (float __steering))
   self)
  (:throttle
   (&optional __throttle)
   (if __throttle (setq _throttle __throttle)) _throttle)
  (:steering
   (&optional __steering)
   (if __steering (setq _steering __steering)) _steering)
  (:serialization-length
   ()
   (+
    ;; float64 _throttle
    8
    ;; float64 _steering
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _throttle
       (sys::poke _throttle (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _steering
       (sys::poke _steering (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _throttle
     (setq _throttle (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _steering
     (setq _steering (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get mymsgs_module::car_command :md5sum-) "39f463d271c2ca10c14182802c72c029")
(setf (get mymsgs_module::car_command :datatype-) "mymsgs_module/car_command")
(setf (get mymsgs_module::car_command :definition-)
      "float64 throttle          # throttle pedal, 1->full acceleration, -1->full brake (adimensional)
float64 steering    # wheels steering angle                                (rad)
")



(provide :mymsgs_module/car_command "39f463d271c2ca10c14182802c72c029")


