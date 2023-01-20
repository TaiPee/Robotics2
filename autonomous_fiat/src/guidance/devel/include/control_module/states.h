// Generated by gencpp from file control_module/states.msg
// DO NOT EDIT!


#ifndef CONTROL_MODULE_MESSAGE_STATES_H
#define CONTROL_MODULE_MESSAGE_STATES_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace control_module
{
template <class ContainerAllocator>
struct states_
{
  typedef states_<ContainerAllocator> Type;

  states_()
    : X(0.0)
    , Y(0.0)
    , Psi(0.0)
    , vx(0.0)
    , vy(0.0)
    , r(0.0)  {
    }
  states_(const ContainerAllocator& _alloc)
    : X(0.0)
    , Y(0.0)
    , Psi(0.0)
    , vx(0.0)
    , vy(0.0)
    , r(0.0)  {
  (void)_alloc;
    }



   typedef double _X_type;
  _X_type X;

   typedef double _Y_type;
  _Y_type Y;

   typedef double _Psi_type;
  _Psi_type Psi;

   typedef double _vx_type;
  _vx_type vx;

   typedef double _vy_type;
  _vy_type vy;

   typedef double _r_type;
  _r_type r;





  typedef boost::shared_ptr< ::control_module::states_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::control_module::states_<ContainerAllocator> const> ConstPtr;

}; // struct states_

typedef ::control_module::states_<std::allocator<void> > states;

typedef boost::shared_ptr< ::control_module::states > statesPtr;
typedef boost::shared_ptr< ::control_module::states const> statesConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::control_module::states_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::control_module::states_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::control_module::states_<ContainerAllocator1> & lhs, const ::control_module::states_<ContainerAllocator2> & rhs)
{
  return lhs.X == rhs.X &&
    lhs.Y == rhs.Y &&
    lhs.Psi == rhs.Psi &&
    lhs.vx == rhs.vx &&
    lhs.vy == rhs.vy &&
    lhs.r == rhs.r;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::control_module::states_<ContainerAllocator1> & lhs, const ::control_module::states_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace control_module

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::control_module::states_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::control_module::states_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::control_module::states_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::control_module::states_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::control_module::states_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::control_module::states_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::control_module::states_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7dbb6f23f56b5fc79fd77870bcc99522";
  }

  static const char* value(const ::control_module::states_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7dbb6f23f56b5fc7ULL;
  static const uint64_t static_value2 = 0x9fd77870bcc99522ULL;
};

template<class ContainerAllocator>
struct DataType< ::control_module::states_<ContainerAllocator> >
{
  static const char* value()
  {
    return "control_module/states";
  }

  static const char* value(const ::control_module::states_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::control_module::states_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 X         # X-coordinate position in the world        (m)\n"
"float64 Y         # Y-coordinate position in the world        (m)\n"
"float64 Psi       # yaw angle of the car in the world         (rad)\n"
"float64 vx        # longitudinal velocity in x, local frame   (m/s)\n"
"float64 vy        # lateral velocity in y, local frame        (m/s)\n"
"float64 r         # yaw rate                                  (rad/s)\n"
;
  }

  static const char* value(const ::control_module::states_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::control_module::states_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.X);
      stream.next(m.Y);
      stream.next(m.Psi);
      stream.next(m.vx);
      stream.next(m.vy);
      stream.next(m.r);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct states_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::control_module::states_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::control_module::states_<ContainerAllocator>& v)
  {
    s << indent << "X: ";
    Printer<double>::stream(s, indent + "  ", v.X);
    s << indent << "Y: ";
    Printer<double>::stream(s, indent + "  ", v.Y);
    s << indent << "Psi: ";
    Printer<double>::stream(s, indent + "  ", v.Psi);
    s << indent << "vx: ";
    Printer<double>::stream(s, indent + "  ", v.vx);
    s << indent << "vy: ";
    Printer<double>::stream(s, indent + "  ", v.vy);
    s << indent << "r: ";
    Printer<double>::stream(s, indent + "  ", v.r);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CONTROL_MODULE_MESSAGE_STATES_H