;; Auto-generated. Do not edit!


(when (boundp 'sensor_fusion::states)
  (if (not (find-package "SENSOR_FUSION"))
    (make-package "SENSOR_FUSION"))
  (shadow 'states (find-package "SENSOR_FUSION")))
(unless (find-package "SENSOR_FUSION::STATES")
  (make-package "SENSOR_FUSION::STATES"))

(in-package "ROS")
;;//! \htmlinclude states.msg.html


(defclass sensor_fusion::states
  :super ros::object
  :slots (_X _Y _Psi _vx _vy _r ))

(defmethod sensor_fusion::states
  (:init
   (&key
    ((:X __X) 0.0)
    ((:Y __Y) 0.0)
    ((:Psi __Psi) 0.0)
    ((:vx __vx) 0.0)
    ((:vy __vy) 0.0)
    ((:r __r) 0.0)
    )
   (send-super :init)
   (setq _X (float __X))
   (setq _Y (float __Y))
   (setq _Psi (float __Psi))
   (setq _vx (float __vx))
   (setq _vy (float __vy))
   (setq _r (float __r))
   self)
  (:X
   (&optional __X)
   (if __X (setq _X __X)) _X)
  (:Y
   (&optional __Y)
   (if __Y (setq _Y __Y)) _Y)
  (:Psi
   (&optional __Psi)
   (if __Psi (setq _Psi __Psi)) _Psi)
  (:vx
   (&optional __vx)
   (if __vx (setq _vx __vx)) _vx)
  (:vy
   (&optional __vy)
   (if __vy (setq _vy __vy)) _vy)
  (:r
   (&optional __r)
   (if __r (setq _r __r)) _r)
  (:serialization-length
   ()
   (+
    ;; float64 _X
    8
    ;; float64 _Y
    8
    ;; float64 _Psi
    8
    ;; float64 _vx
    8
    ;; float64 _vy
    8
    ;; float64 _r
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _X
       (sys::poke _X (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Y
       (sys::poke _Y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _Psi
       (sys::poke _Psi (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _vx
       (sys::poke _vx (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _vy
       (sys::poke _vy (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _r
       (sys::poke _r (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _X
     (setq _X (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Y
     (setq _Y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _Psi
     (setq _Psi (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _vx
     (setq _vx (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _vy
     (setq _vy (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _r
     (setq _r (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get sensor_fusion::states :md5sum-) "7dbb6f23f56b5fc79fd77870bcc99522")
(setf (get sensor_fusion::states :datatype-) "sensor_fusion/states")
(setf (get sensor_fusion::states :definition-)
      "float64 X         # X-coordinate position in the world        (m)
float64 Y         # Y-coordinate position in the world        (m)
float64 Psi       # yaw angle of the car in the world         (rad)
float64 vx        # longitudinal velocity in x, local frame   (m/s)
float64 vy        # lateral velocity in y, local frame        (m/s)
float64 r         # yaw rate                                  (rad/s)
")



(provide :sensor_fusion/states "7dbb6f23f56b5fc79fd77870bcc99522")


