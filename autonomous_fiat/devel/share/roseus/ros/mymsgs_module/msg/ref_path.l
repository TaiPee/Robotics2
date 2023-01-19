;; Auto-generated. Do not edit!


(when (boundp 'mymsgs_module::ref_path)
  (if (not (find-package "MYMSGS_MODULE"))
    (make-package "MYMSGS_MODULE"))
  (shadow 'ref_path (find-package "MYMSGS_MODULE")))
(unless (find-package "MYMSGS_MODULE::REF_PATH")
  (make-package "MYMSGS_MODULE::REF_PATH"))

(in-package "ROS")
;;//! \htmlinclude ref_path.msg.html


(defclass mymsgs_module::ref_path
  :super ros::object
  :slots (_points ))

(defmethod mymsgs_module::ref_path
  (:init
   (&key
    ((:points __points) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _points __points)
   self)
  (:points
   (&optional __points)
   (if __points (setq _points __points)) _points)
  (:serialization-length
   ()
   (+
    ;; float32[] _points
    (* 4    (length _points)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[] _points
     (write-long (length _points) s)
     (dotimes (i (length _points))
       (sys::poke (elt _points i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[] _points
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _points (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _points i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get mymsgs_module::ref_path :md5sum-) "93c76054c676123f8fabd76bcbdae971")
(setf (get mymsgs_module::ref_path :datatype-) "mymsgs_module/ref_path")
(setf (get mymsgs_module::ref_path :definition-)
      "float32[] points
")



(provide :mymsgs_module/ref_path "93c76054c676123f8fabd76bcbdae971")


