#!/usr/bin/python

import rospy
import serial
import struct

from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

cmd_byte_map = {
    'servo_U' : b"\x02",
    'servo_L' : b"\x04"
}

def main():
    rospy.init_node("simple_drive")
    
    baudrate = rospy.get_param('~baudrate', 9600)
    Serial = serial.Serial(baudrate=baudrate)
    Serial.port = rospy.get_param("~serial_dev")
    Serial.open()
    

    def on_new_servo_T(data):
        serial_msg = cmd_byte_map['servo_U'] + struct.pack("<f", data.data)
        Serial.write(serial_msg)

    def on_new_servo_B(data):
        serial_msg = cmd_byte_map['servo_L'] + struct.pack("<f", data.data)
        Serial.write(serial_msg)




    subscriber_servo_U = rospy.Subscriber("servo_pos_U", Float32, on_new_servo_T, queue_size=10)
    subscriber_servo_L = rospy.Subscriber("servo_pos_L", Float32, on_new_servo_B, queue_size=10)


    rospy.spin()
