// Generated by gencpp from file mymsgs_module/control_command.msg
// DO NOT EDIT!


#ifndef MYMSGS_MODULE_MESSAGE_CONTROL_COMMAND_H
#define MYMSGS_MODULE_MESSAGE_CONTROL_COMMAND_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace mymsgs_module
{
template <class ContainerAllocator>
struct control_command_
{
  typedef control_command_<ContainerAllocator> Type;

  control_command_()
    : velocity(0.0)
    , steering(0.0)  {
    }
  control_command_(const ContainerAllocator& _alloc)
    : velocity(0.0)
    , steering(0.0)  {
  (void)_alloc;
    }



   typedef double _velocity_type;
  _velocity_type velocity;

   typedef double _steering_type;
  _steering_type steering;





  typedef boost::shared_ptr< ::mymsgs_module::control_command_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mymsgs_module::control_command_<ContainerAllocator> const> ConstPtr;

}; // struct control_command_

typedef ::mymsgs_module::control_command_<std::allocator<void> > control_command;

typedef boost::shared_ptr< ::mymsgs_module::control_command > control_commandPtr;
typedef boost::shared_ptr< ::mymsgs_module::control_command const> control_commandConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mymsgs_module::control_command_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mymsgs_module::control_command_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::mymsgs_module::control_command_<ContainerAllocator1> & lhs, const ::mymsgs_module::control_command_<ContainerAllocator2> & rhs)
{
  return lhs.velocity == rhs.velocity &&
    lhs.steering == rhs.steering;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::mymsgs_module::control_command_<ContainerAllocator1> & lhs, const ::mymsgs_module::control_command_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace mymsgs_module

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::mymsgs_module::control_command_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mymsgs_module::control_command_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mymsgs_module::control_command_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mymsgs_module::control_command_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mymsgs_module::control_command_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mymsgs_module::control_command_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mymsgs_module::control_command_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2cccf116fd404cf82580c85a4b8c480d";
  }

  static const char* value(const ::mymsgs_module::control_command_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2cccf116fd404cf8ULL;
  static const uint64_t static_value2 = 0x2580c85a4b8c480dULL;
};

template<class ContainerAllocator>
struct DataType< ::mymsgs_module::control_command_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mymsgs_module/control_command";
  }

  static const char* value(const ::mymsgs_module::control_command_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mymsgs_module::control_command_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 velocity          # desired velocity        (m/s)\n"
"float64 steering    # wheels steering angle   (rad)\n"
;
  }

  static const char* value(const ::mymsgs_module::control_command_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mymsgs_module::control_command_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.velocity);
      stream.next(m.steering);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct control_command_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mymsgs_module::control_command_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mymsgs_module::control_command_<ContainerAllocator>& v)
  {
    s << indent << "velocity: ";
    Printer<double>::stream(s, indent + "  ", v.velocity);
    s << indent << "steering: ";
    Printer<double>::stream(s, indent + "  ", v.steering);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MYMSGS_MODULE_MESSAGE_CONTROL_COMMAND_H
