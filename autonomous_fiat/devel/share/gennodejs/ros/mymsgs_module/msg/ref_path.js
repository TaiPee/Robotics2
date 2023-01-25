// Auto-generated. Do not edit!

// (in-package mymsgs_module.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class ref_path {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.points = null;
    }
    else {
      if (initObj.hasOwnProperty('points')) {
        this.points = initObj.points
      }
      else {
        this.points = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ref_path
    // Serialize message field [points]
    bufferOffset = _arraySerializer.float32(obj.points, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ref_path
    let len;
    let data = new ref_path(null);
    // Deserialize message field [points]
    data.points = _arrayDeserializer.float32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.points.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mymsgs_module/ref_path';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '93c76054c676123f8fabd76bcbdae971';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32[] points
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ref_path(null);
    if (msg.points !== undefined) {
      resolved.points = msg.points;
    }
    else {
      resolved.points = []
    }

    return resolved;
    }
};

module.exports = ref_path;
