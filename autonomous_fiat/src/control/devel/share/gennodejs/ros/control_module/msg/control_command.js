// Auto-generated. Do not edit!

// (in-package control_module.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class control_command {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.throttle = null;
      this.steering_angle = null;
    }
    else {
      if (initObj.hasOwnProperty('throttle')) {
        this.throttle = initObj.throttle
      }
      else {
        this.throttle = 0.0;
      }
      if (initObj.hasOwnProperty('steering_angle')) {
        this.steering_angle = initObj.steering_angle
      }
      else {
        this.steering_angle = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type control_command
    // Serialize message field [throttle]
    bufferOffset = _serializer.float64(obj.throttle, buffer, bufferOffset);
    // Serialize message field [steering_angle]
    bufferOffset = _serializer.float64(obj.steering_angle, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type control_command
    let len;
    let data = new control_command(null);
    // Deserialize message field [throttle]
    data.throttle = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [steering_angle]
    data.steering_angle = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'control_module/control_command';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '9f3b540e5265853adbd53f61d05b89c6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 throttle          # throttle pedal, 1->full acceleration, -1->full brake (adimensional)
    float64 steering_angle    # wheels steering angle                                (rad)
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new control_command(null);
    if (msg.throttle !== undefined) {
      resolved.throttle = msg.throttle;
    }
    else {
      resolved.throttle = 0.0
    }

    if (msg.steering_angle !== undefined) {
      resolved.steering_angle = msg.steering_angle;
    }
    else {
      resolved.steering_angle = 0.0
    }

    return resolved;
    }
};

module.exports = control_command;
