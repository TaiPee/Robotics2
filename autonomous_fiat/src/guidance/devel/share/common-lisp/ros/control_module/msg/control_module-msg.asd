
(cl:in-package :asdf)

(defsystem "control_module-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "control_command" :depends-on ("_package_control_command"))
    (:file "_package_control_command" :depends-on ("_package"))
    (:file "states" :depends-on ("_package_states"))
    (:file "_package_states" :depends-on ("_package"))
  ))