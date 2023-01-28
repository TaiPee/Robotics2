# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "mymsgs_module: 4 messages, 0 services")

set(MSG_I_FLAGS "-Imymsgs_module:/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(mymsgs_module_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/control_command.msg" NAME_WE)
add_custom_target(_mymsgs_module_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "mymsgs_module" "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/control_command.msg" ""
)

get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/car_command.msg" NAME_WE)
add_custom_target(_mymsgs_module_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "mymsgs_module" "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/car_command.msg" ""
)

get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/states.msg" NAME_WE)
add_custom_target(_mymsgs_module_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "mymsgs_module" "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/states.msg" ""
)

get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/ref_path.msg" NAME_WE)
add_custom_target(_mymsgs_module_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "mymsgs_module" "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/ref_path.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/control_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mymsgs_module
)
_generate_msg_cpp(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/car_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mymsgs_module
)
_generate_msg_cpp(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/states.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mymsgs_module
)
_generate_msg_cpp(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/ref_path.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mymsgs_module
)

### Generating Services

### Generating Module File
_generate_module_cpp(mymsgs_module
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mymsgs_module
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(mymsgs_module_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(mymsgs_module_generate_messages mymsgs_module_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/control_command.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_cpp _mymsgs_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/car_command.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_cpp _mymsgs_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/states.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_cpp _mymsgs_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/ref_path.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_cpp _mymsgs_module_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mymsgs_module_gencpp)
add_dependencies(mymsgs_module_gencpp mymsgs_module_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mymsgs_module_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/control_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mymsgs_module
)
_generate_msg_eus(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/car_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mymsgs_module
)
_generate_msg_eus(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/states.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mymsgs_module
)
_generate_msg_eus(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/ref_path.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mymsgs_module
)

### Generating Services

### Generating Module File
_generate_module_eus(mymsgs_module
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mymsgs_module
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(mymsgs_module_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(mymsgs_module_generate_messages mymsgs_module_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/control_command.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_eus _mymsgs_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/car_command.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_eus _mymsgs_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/states.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_eus _mymsgs_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/ref_path.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_eus _mymsgs_module_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mymsgs_module_geneus)
add_dependencies(mymsgs_module_geneus mymsgs_module_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mymsgs_module_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/control_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mymsgs_module
)
_generate_msg_lisp(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/car_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mymsgs_module
)
_generate_msg_lisp(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/states.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mymsgs_module
)
_generate_msg_lisp(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/ref_path.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mymsgs_module
)

### Generating Services

### Generating Module File
_generate_module_lisp(mymsgs_module
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mymsgs_module
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(mymsgs_module_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(mymsgs_module_generate_messages mymsgs_module_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/control_command.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_lisp _mymsgs_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/car_command.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_lisp _mymsgs_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/states.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_lisp _mymsgs_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/ref_path.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_lisp _mymsgs_module_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mymsgs_module_genlisp)
add_dependencies(mymsgs_module_genlisp mymsgs_module_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mymsgs_module_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/control_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mymsgs_module
)
_generate_msg_nodejs(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/car_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mymsgs_module
)
_generate_msg_nodejs(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/states.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mymsgs_module
)
_generate_msg_nodejs(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/ref_path.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mymsgs_module
)

### Generating Services

### Generating Module File
_generate_module_nodejs(mymsgs_module
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mymsgs_module
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(mymsgs_module_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(mymsgs_module_generate_messages mymsgs_module_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/control_command.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_nodejs _mymsgs_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/car_command.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_nodejs _mymsgs_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/states.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_nodejs _mymsgs_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/ref_path.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_nodejs _mymsgs_module_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mymsgs_module_gennodejs)
add_dependencies(mymsgs_module_gennodejs mymsgs_module_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mymsgs_module_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/control_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mymsgs_module
)
_generate_msg_py(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/car_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mymsgs_module
)
_generate_msg_py(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/states.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mymsgs_module
)
_generate_msg_py(mymsgs_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/ref_path.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mymsgs_module
)

### Generating Services

### Generating Module File
_generate_module_py(mymsgs_module
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mymsgs_module
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(mymsgs_module_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(mymsgs_module_generate_messages mymsgs_module_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/control_command.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_py _mymsgs_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/car_command.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_py _mymsgs_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/states.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_py _mymsgs_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/mymsgs/msg/ref_path.msg" NAME_WE)
add_dependencies(mymsgs_module_generate_messages_py _mymsgs_module_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mymsgs_module_genpy)
add_dependencies(mymsgs_module_genpy mymsgs_module_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mymsgs_module_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mymsgs_module)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mymsgs_module
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(mymsgs_module_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(mymsgs_module_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mymsgs_module)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mymsgs_module
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(mymsgs_module_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(mymsgs_module_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mymsgs_module)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mymsgs_module
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(mymsgs_module_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(mymsgs_module_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mymsgs_module)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mymsgs_module
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(mymsgs_module_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(mymsgs_module_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mymsgs_module)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mymsgs_module\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mymsgs_module
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(mymsgs_module_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(mymsgs_module_generate_messages_py geometry_msgs_generate_messages_py)
endif()
