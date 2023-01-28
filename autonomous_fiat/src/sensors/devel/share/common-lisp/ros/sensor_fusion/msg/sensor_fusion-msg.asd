
(cl:in-package :asdf)

(defsystem "sensor_fusion-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "car_command" :depends-on ("_package_car_command"))
    (:file "_package_car_command" :depends-on ("_package"))
    (:file "control_command" :depends-on ("_package_control_command"))
    (:file "_package_control_command" :depends-on ("_package"))
    (:file "ref_path" :depends-on ("_package_ref_path"))
    (:file "_package_ref_path" :depends-on ("_package"))
    (:file "states" :depends-on ("_package_states"))
    (:file "_package_states" :depends-on ("_package"))
  ))