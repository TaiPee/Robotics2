# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "control_module: 2 messages, 0 services")

set(MSG_I_FLAGS "-Icontrol_module:/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(control_module_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/states.msg" NAME_WE)
add_custom_target(_control_module_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "control_module" "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/states.msg" ""
)

get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/control_command.msg" NAME_WE)
add_custom_target(_control_module_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "control_module" "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/control_command.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(control_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/control_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/control_module
)
_generate_msg_cpp(control_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/states.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/control_module
)

### Generating Services

### Generating Module File
_generate_module_cpp(control_module
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/control_module
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(control_module_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(control_module_generate_messages control_module_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/states.msg" NAME_WE)
add_dependencies(control_module_generate_messages_cpp _control_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/control_command.msg" NAME_WE)
add_dependencies(control_module_generate_messages_cpp _control_module_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(control_module_gencpp)
add_dependencies(control_module_gencpp control_module_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS control_module_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(control_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/control_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/control_module
)
_generate_msg_eus(control_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/states.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/control_module
)

### Generating Services

### Generating Module File
_generate_module_eus(control_module
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/control_module
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(control_module_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(control_module_generate_messages control_module_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/states.msg" NAME_WE)
add_dependencies(control_module_generate_messages_eus _control_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/control_command.msg" NAME_WE)
add_dependencies(control_module_generate_messages_eus _control_module_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(control_module_geneus)
add_dependencies(control_module_geneus control_module_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS control_module_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(control_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/control_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/control_module
)
_generate_msg_lisp(control_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/states.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/control_module
)

### Generating Services

### Generating Module File
_generate_module_lisp(control_module
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/control_module
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(control_module_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(control_module_generate_messages control_module_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/states.msg" NAME_WE)
add_dependencies(control_module_generate_messages_lisp _control_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/control_command.msg" NAME_WE)
add_dependencies(control_module_generate_messages_lisp _control_module_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(control_module_genlisp)
add_dependencies(control_module_genlisp control_module_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS control_module_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(control_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/control_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/control_module
)
_generate_msg_nodejs(control_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/states.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/control_module
)

### Generating Services

### Generating Module File
_generate_module_nodejs(control_module
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/control_module
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(control_module_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(control_module_generate_messages control_module_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/states.msg" NAME_WE)
add_dependencies(control_module_generate_messages_nodejs _control_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/control_command.msg" NAME_WE)
add_dependencies(control_module_generate_messages_nodejs _control_module_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(control_module_gennodejs)
add_dependencies(control_module_gennodejs control_module_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS control_module_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(control_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/control_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/control_module
)
_generate_msg_py(control_module
  "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/states.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/control_module
)

### Generating Services

### Generating Module File
_generate_module_py(control_module
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/control_module
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(control_module_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(control_module_generate_messages control_module_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/states.msg" NAME_WE)
add_dependencies(control_module_generate_messages_py _control_module_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/control/src/msg/control_command.msg" NAME_WE)
add_dependencies(control_module_generate_messages_py _control_module_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(control_module_genpy)
add_dependencies(control_module_genpy control_module_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS control_module_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/control_module)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/control_module
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(control_module_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/control_module)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/control_module
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(control_module_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/control_module)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/control_module
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(control_module_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/control_module)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/control_module
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(control_module_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/control_module)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/control_module\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/control_module
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(control_module_generate_messages_py std_msgs_generate_messages_py)
endif()
