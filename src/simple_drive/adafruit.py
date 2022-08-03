#!/usr/bin/env python3

from adafruit_servokit import ServoKit
import rospy
from std_msgs.msg import Int64, Int32
import time

# Matrix
import board
import neopixel_spi as neopixel
import rospy

def callback_s1(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    print ("entre a callback")
    kit.servo[servo_cero].angle=data.data

def callback_s2(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    print ("entre a callback")
    kit.servo[servo_uno].angle=data.data

def callback_s3(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    print ("entre a callback")
    #kit.servo[servo_dos].angle= data.data
    if (data.data >= -90 and data.data <= 90):
        kit.servo[servo_dos].angle=int(map(data.data, -90, 90, 236, 416))
        kit.servo[servo_dos].duty_cycle = 0

def on_new_led(data):    
    global state
    state = data.data

def change_color(color):
    for i in range(64):
        pixels[i] = COLORS[color]
    pixels.show()
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("servo1", Int64, callback_s1)
    rospy.Subscriber("servo2", Int64, callback_s2)
    rospy.Subscriber("servo3", Int64, callback_s3)
    subscriber_led     = rospy.Subscriber("status_led", Int32, on_new_led, queue_size = 10)
    print ("entre a listener")
    green = False

    while True:
        if state == 3:
            if green:
                change_color(0)
            else:
                change_color(3)
            green = not green
        else:
            change_color(state)
        time.sleep(.5)
    rospy.spin()

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

if __name__ == '__main__':
    """kit = ServoKit(channels=16)
    servo_cero = 0
    servo_uno = 1
    servo_dos = 2
    servo_tres = 15
    kit.servo[servo_dos].set_pulse_width_range(500, 2500)
    kit.servo[servo_dos].actuation_range = 640
    kit.servo[servo_tres].angle=180"""

    # Matrix
    NUM_PIXELS = 64
    PIXEL_ORDER = neopixel.RGB    
    COLORS = (0x000000, 0x0000FF, 0x00FF00, 0xFF0000)
    #Green RED Blue aunque arriba diga RGB XD, esta en bgr pero si lo invierno se vuelve a invertir todo
    spi = board.SPI()
    pixels = neopixel.NeoPixel_SPI(spi, NUM_PIXELS, pixel_order=PIXEL_ORDER, auto_write=False)
    state = 0
    print ("entre a main")
    
    listener()
