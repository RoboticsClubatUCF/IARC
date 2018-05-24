// Auto-generated. Do not edit!

// (in-package custom_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class StateMachine {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.preflight = null;
      this.takeoff = null;
      this.flight = null;
      this.hover = null;
      this.land = null;
      this.emergency = null;
    }
    else {
      if (initObj.hasOwnProperty('preflight')) {
        this.preflight = initObj.preflight
      }
      else {
        this.preflight = false;
      }
      if (initObj.hasOwnProperty('takeoff')) {
        this.takeoff = initObj.takeoff
      }
      else {
        this.takeoff = false;
      }
      if (initObj.hasOwnProperty('flight')) {
        this.flight = initObj.flight
      }
      else {
        this.flight = false;
      }
      if (initObj.hasOwnProperty('hover')) {
        this.hover = initObj.hover
      }
      else {
        this.hover = false;
      }
      if (initObj.hasOwnProperty('land')) {
        this.land = initObj.land
      }
      else {
        this.land = false;
      }
      if (initObj.hasOwnProperty('emergency')) {
        this.emergency = initObj.emergency
      }
      else {
        this.emergency = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type StateMachine
    // Serialize message field [preflight]
    bufferOffset = _serializer.bool(obj.preflight, buffer, bufferOffset);
    // Serialize message field [takeoff]
    bufferOffset = _serializer.bool(obj.takeoff, buffer, bufferOffset);
    // Serialize message field [flight]
    bufferOffset = _serializer.bool(obj.flight, buffer, bufferOffset);
    // Serialize message field [hover]
    bufferOffset = _serializer.bool(obj.hover, buffer, bufferOffset);
    // Serialize message field [land]
    bufferOffset = _serializer.bool(obj.land, buffer, bufferOffset);
    // Serialize message field [emergency]
    bufferOffset = _serializer.bool(obj.emergency, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type StateMachine
    let len;
    let data = new StateMachine(null);
    // Deserialize message field [preflight]
    data.preflight = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [takeoff]
    data.takeoff = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [flight]
    data.flight = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [hover]
    data.hover = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [land]
    data.land = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [emergency]
    data.emergency = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 6;
  }

  static datatype() {
    // Returns string type for a message object
    return 'custom_msgs/StateMachine';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3f8a4c584aa1c1f432d46d2dd0cd69f1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool preflight
    bool takeoff
    bool flight
    bool hover
    bool land
    bool emergency
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new StateMachine(null);
    if (msg.preflight !== undefined) {
      resolved.preflight = msg.preflight;
    }
    else {
      resolved.preflight = false
    }

    if (msg.takeoff !== undefined) {
      resolved.takeoff = msg.takeoff;
    }
    else {
      resolved.takeoff = false
    }

    if (msg.flight !== undefined) {
      resolved.flight = msg.flight;
    }
    else {
      resolved.flight = false
    }

    if (msg.hover !== undefined) {
      resolved.hover = msg.hover;
    }
    else {
      resolved.hover = false
    }

    if (msg.land !== undefined) {
      resolved.land = msg.land;
    }
    else {
      resolved.land = false
    }

    if (msg.emergency !== undefined) {
      resolved.emergency = msg.emergency;
    }
    else {
      resolved.emergency = false
    }

    return resolved;
    }
};

module.exports = StateMachine;
