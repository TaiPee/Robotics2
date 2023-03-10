// Generated by gencpp from file mymsgs_module/ref_path.msg
// DO NOT EDIT!


#ifndef MYMSGS_MODULE_MESSAGE_REF_PATH_H
#define MYMSGS_MODULE_MESSAGE_REF_PATH_H


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
struct ref_path_
{
  typedef ref_path_<ContainerAllocator> Type;

  ref_path_()
    : points()  {
    }
  ref_path_(const ContainerAllocator& _alloc)
    : points(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _points_type;
  _points_type points;





  typedef boost::shared_ptr< ::mymsgs_module::ref_path_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mymsgs_module::ref_path_<ContainerAllocator> const> ConstPtr;

}; // struct ref_path_

typedef ::mymsgs_module::ref_path_<std::allocator<void> > ref_path;

typedef boost::shared_ptr< ::mymsgs_module::ref_path > ref_pathPtr;
typedef boost::shared_ptr< ::mymsgs_module::ref_path const> ref_pathConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mymsgs_module::ref_path_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mymsgs_module::ref_path_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::mymsgs_module::ref_path_<ContainerAllocator1> & lhs, const ::mymsgs_module::ref_path_<ContainerAllocator2> & rhs)
{
  return lhs.points == rhs.points;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::mymsgs_module::ref_path_<ContainerAllocator1> & lhs, const ::mymsgs_module::ref_path_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace mymsgs_module

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::mymsgs_module::ref_path_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mymsgs_module::ref_path_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mymsgs_module::ref_path_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mymsgs_module::ref_path_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mymsgs_module::ref_path_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mymsgs_module::ref_path_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mymsgs_module::ref_path_<ContainerAllocator> >
{
  static const char* value()
  {
    return "93c76054c676123f8fabd76bcbdae971";
  }

  static const char* value(const ::mymsgs_module::ref_path_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x93c76054c676123fULL;
  static const uint64_t static_value2 = 0x8fabd76bcbdae971ULL;
};

template<class ContainerAllocator>
struct DataType< ::mymsgs_module::ref_path_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mymsgs_module/ref_path";
  }

  static const char* value(const ::mymsgs_module::ref_path_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mymsgs_module::ref_path_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32[] points\n"
;
  }

  static const char* value(const ::mymsgs_module::ref_path_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mymsgs_module::ref_path_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.points);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ref_path_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mymsgs_module::ref_path_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mymsgs_module::ref_path_<ContainerAllocator>& v)
  {
    s << indent << "points[]" << std::endl;
    for (size_t i = 0; i < v.points.size(); ++i)
    {
      s << indent << "  points[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.points[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // MYMSGS_MODULE_MESSAGE_REF_PATH_H
