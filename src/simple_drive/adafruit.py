#!/usr/bin/env python3

from adafruit_servokit import ServoKit
import rospy
from std_msgs.msg import Int64, Int32

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
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    if (data.data == 0):
        pixels[	0	] = COLORS [0]
        pixels[	1	] = COLORS [0]
        pixels[	2	] = COLORS [0]
        pixels[	3	] = COLORS [0]
        pixels[	4	] = COLORS [0]
        pixels[	5	] = COLORS [0]
        pixels[	6	] = COLORS [0]
        pixels[	7	] = COLORS [0]
        pixels[	8	] = COLORS [0]
        pixels[	9	] = COLORS [0]
        pixels[	10	] = COLORS [0]
        pixels[	11	] = COLORS [0]
        pixels[	12	] = COLORS [0]
        pixels[	13	] = COLORS [0]
        pixels[	14	] = COLORS [0]
        pixels[	15	] = COLORS [0]
        pixels[	16	] = COLORS [0]
        pixels[	17	] = COLORS [0]
        pixels[	18	] = COLORS [0]
        pixels[	19	] = COLORS [0]
        pixels[	20	] = COLORS [0]
        pixels[	21	] = COLORS [0]
        pixels[	22	] = COLORS [0]
        pixels[	23	] = COLORS [0]
        pixels[	24	] = COLORS [0]
        pixels[	25	] = COLORS [0]
        pixels[	26	] = COLORS [0]
        pixels[	27	] = COLORS [0]
        pixels[	28	] = COLORS [0]
        pixels[	29	] = COLORS [0]
        pixels[	30	] = COLORS [0]
        pixels[	31	] = COLORS [0]
        pixels[	32	] = COLORS [0]
        pixels[	33	] = COLORS [0]
        pixels[	34	] = COLORS [0]
        pixels[	35	] = COLORS [0]
        pixels[	36	] = COLORS [0]
        pixels[	37	] = COLORS [0]
        pixels[	38	] = COLORS [0]
        pixels[	39	] = COLORS [0]
        pixels[	40	] = COLORS [0]
        pixels[	41	] = COLORS [0]
        pixels[	42	] = COLORS [0]
        pixels[	43	] = COLORS [0]
        pixels[	44	] = COLORS [0]
        pixels[	45	] = COLORS [0]
        pixels[	46	] = COLORS [0]
        pixels[	47	] = COLORS [0]
        pixels[	48	] = COLORS [0]
        pixels[	49	] = COLORS [0]
        pixels[	50	] = COLORS [0]
        pixels[	51	] = COLORS [0]
        pixels[	52	] = COLORS [0]
        pixels[	53	] = COLORS [0]
        pixels[	54	] = COLORS [0]
        pixels[	55	] = COLORS [0]
        pixels[	56	] = COLORS [0]
        pixels[	57	] = COLORS [0]
        pixels[	58	] = COLORS [0]
        pixels[	59	] = COLORS [0]
        pixels[	60	] = COLORS [0]
        pixels[	61	] = COLORS [0]
        pixels[	62	] = COLORS [0]
        pixels[	63	] = COLORS [0]

        pixels.show()
    elif (data.data == 1):
        pixels[	0	] = COLORS [1]
        pixels[	1	] = COLORS [1]
        pixels[	2	] = COLORS [1]
        pixels[	3	] = COLORS [1]
        pixels[	4	] = COLORS [1]
        pixels[	5	] = COLORS [1]
        pixels[	6	] = COLORS [1]
        pixels[	7	] = COLORS [1]
        pixels[	8	] = COLORS [1]
        pixels[	9	] = COLORS [1]
        pixels[	10	] = COLORS [1]
        pixels[	11	] = COLORS [1]
        pixels[	12	] = COLORS [1]
        pixels[	13	] = COLORS [1]
        pixels[	14	] = COLORS [1]
        pixels[	15	] = COLORS [1]
        pixels[	16	] = COLORS [1]
        pixels[	17	] = COLORS [1]
        pixels[	18	] = COLORS [1]
        pixels[	19	] = COLORS [1]
        pixels[	20	] = COLORS [1]
        pixels[	21	] = COLORS [1]
        pixels[	22	] = COLORS [1]
        pixels[	23	] = COLORS [1]
        pixels[	24	] = COLORS [1]
        pixels[	25	] = COLORS [1]
        pixels[	26	] = COLORS [1]
        pixels[	27	] = COLORS [1]
        pixels[	28	] = COLORS [1]
        pixels[	29	] = COLORS [1]
        pixels[	30	] = COLORS [1]
        pixels[	31	] = COLORS [1]
        pixels[	32	] = COLORS [1]
        pixels[	33	] = COLORS [1]
        pixels[	34	] = COLORS [1]
        pixels[	35	] = COLORS [1]
        pixels[	36	] = COLORS [1]
        pixels[	37	] = COLORS [1]
        pixels[	38	] = COLORS [1]
        pixels[	39	] = COLORS [1]
        pixels[	40	] = COLORS [1]
        pixels[	41	] = COLORS [1]
        pixels[	42	] = COLORS [1]
        pixels[	43	] = COLORS [1]
        pixels[	44	] = COLORS [1]
        pixels[	45	] = COLORS [1]
        pixels[	46	] = COLORS [1]
        pixels[	47	] = COLORS [1]
        pixels[	48	] = COLORS [1]
        pixels[	49	] = COLORS [1]
        pixels[	50	] = COLORS [1]
        pixels[	51	] = COLORS [1]
        pixels[	52	] = COLORS [1]
        pixels[	53	] = COLORS [1]
        pixels[	54	] = COLORS [1]
        pixels[	55	] = COLORS [1]
        pixels[	56	] = COLORS [1]
        pixels[	57	] = COLORS [1]
        pixels[	58	] = COLORS [1]
        pixels[	59	] = COLORS [1]
        pixels[	60	] = COLORS [1]
        pixels[	61	] = COLORS [1]
        pixels[	62	] = COLORS [1]
        pixels[	63	] = COLORS [1]

        pixels.show()
    elif (data.data == 2):
        pixels[	0	] = COLORS [2]
        pixels[	1	] = COLORS [2]
        pixels[	2	] = COLORS [2]
        pixels[	3	] = COLORS [2]
        pixels[	4	] = COLORS [2]
        pixels[	5	] = COLORS [2]
        pixels[	6	] = COLORS [2]
        pixels[	7	] = COLORS [2]
        pixels[	8	] = COLORS [2]
        pixels[	9	] = COLORS [2]
        pixels[	10	] = COLORS [2]
        pixels[	11	] = COLORS [2]
        pixels[	12	] = COLORS [2]
        pixels[	13	] = COLORS [2]
        pixels[	14	] = COLORS [2]
        pixels[	15	] = COLORS [2]
        pixels[	16	] = COLORS [2]
        pixels[	17	] = COLORS [2]
        pixels[	18	] = COLORS [2]
        pixels[	19	] = COLORS [2]
        pixels[	20	] = COLORS [2]
        pixels[	21	] = COLORS [2]
        pixels[	22	] = COLORS [2]
        pixels[	23	] = COLORS [2]
        pixels[	24	] = COLORS [2]
        pixels[	25	] = COLORS [2]
        pixels[	26	] = COLORS [2]
        pixels[	27	] = COLORS [2]
        pixels[	28	] = COLORS [2]
        pixels[	29	] = COLORS [2]
        pixels[	30	] = COLORS [2]
        pixels[	31	] = COLORS [2]
        pixels[	32	] = COLORS [2]
        pixels[	33	] = COLORS [2]
        pixels[	34	] = COLORS [2]
        pixels[	35	] = COLORS [2]
        pixels[	36	] = COLORS [2]
        pixels[	37	] = COLORS [2]
        pixels[	38	] = COLORS [2]
        pixels[	39	] = COLORS [2]
        pixels[	40	] = COLORS [2]
        pixels[	41	] = COLORS [2]
        pixels[	42	] = COLORS [2]
        pixels[	43	] = COLORS [2]
        pixels[	44	] = COLORS [2]
        pixels[	45	] = COLORS [2]
        pixels[	46	] = COLORS [2]
        pixels[	47	] = COLORS [2]
        pixels[	48	] = COLORS [2]
        pixels[	49	] = COLORS [2]
        pixels[	50	] = COLORS [2]
        pixels[	51	] = COLORS [2]
        pixels[	52	] = COLORS [2]
        pixels[	53	] = COLORS [2]
        pixels[	54	] = COLORS [2]
        pixels[	55	] = COLORS [2]
        pixels[	56	] = COLORS [2]
        pixels[	57	] = COLORS [2]
        pixels[	58	] = COLORS [2]
        pixels[	59	] = COLORS [2]
        pixels[	60	] = COLORS [2]
        pixels[	61	] = COLORS [2]
        pixels[	62	] = COLORS [2]
        pixels[	63	] = COLORS [2]

        pixels.show() 
    elif (data.data == 3):
        pixels[	0	] = COLORS [3]
        pixels[	1	] = COLORS [3]
        pixels[	2	] = COLORS [3]
        pixels[	3	] = COLORS [3]
        pixels[	4	] = COLORS [3]
        pixels[	5	] = COLORS [3]
        pixels[	6	] = COLORS [3]
        pixels[	7	] = COLORS [3]
        pixels[	8	] = COLORS [3]
        pixels[	9	] = COLORS [3]
        pixels[	10	] = COLORS [3]
        pixels[	11	] = COLORS [3]
        pixels[	12	] = COLORS [3]
        pixels[	13	] = COLORS [3]
        pixels[	14	] = COLORS [3]
        pixels[	15	] = COLORS [3]
        pixels[	16	] = COLORS [3]
        pixels[	17	] = COLORS [3]
        pixels[	18	] = COLORS [3]
        pixels[	19	] = COLORS [3]
        pixels[	20	] = COLORS [3]
        pixels[	21	] = COLORS [3]
        pixels[	22	] = COLORS [3]
        pixels[	23	] = COLORS [3]
        pixels[	24	] = COLORS [3]
        pixels[	25	] = COLORS [3]
        pixels[	26	] = COLORS [3]
        pixels[	27	] = COLORS [3]
        pixels[	28	] = COLORS [3]
        pixels[	29	] = COLORS [3]
        pixels[	30	] = COLORS [3]
        pixels[	31	] = COLORS [3]
        pixels[	32	] = COLORS [3]
        pixels[	33	] = COLORS [3]
        pixels[	34	] = COLORS [3]
        pixels[	35	] = COLORS [3]
        pixels[	36	] = COLORS [3]
        pixels[	37	] = COLORS [3]
        pixels[	38	] = COLORS [3]
        pixels[	39	] = COLORS [3]
        pixels[	40	] = COLORS [3]
        pixels[	41	] = COLORS [3]
        pixels[	42	] = COLORS [3]
        pixels[	43	] = COLORS [3]
        pixels[	44	] = COLORS [3]
        pixels[	45	] = COLORS [3]
        pixels[	46	] = COLORS [3]
        pixels[	47	] = COLORS [3]
        pixels[	48	] = COLORS [3]
        pixels[	49	] = COLORS [3]
        pixels[	50	] = COLORS [3]
        pixels[	51	] = COLORS [3]
        pixels[	52	] = COLORS [3]
        pixels[	53	] = COLORS [3]
        pixels[	54	] = COLORS [3]
        pixels[	55	] = COLORS [3]
        pixels[	56	] = COLORS [3]
        pixels[	57	] = COLORS [3]
        pixels[	58	] = COLORS [3]
        pixels[	59	] = COLORS [3]
        pixels[	60	] = COLORS [3]
        pixels[	61	] = COLORS [3]
        pixels[	62	] = COLORS [3]
        pixels[	63	] = COLORS [3]

        pixels.show()   


    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("servo1", Int64, callback_s1)
    rospy.Subscriber("servo2", Int64, callback_s2)
    rospy.Subscriber("servo3", Int64, callback_s3)
    subscriber_led     = rospy.Subscriber("status_led", Int32, on_new_led, queue_size = 10)
    print ("entre a listener")

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
    COLORS = (0x000000, 0xFF0000, 0x00FF00, 0x0000FF)
    #Green RED Blue aunque arriba diga RGB XD, esta en bgr pero si lo invierno se vuelve a invertir todo
    spi = board.SPI()
    pixels = neopixel.NeoPixel_SPI(spi, NUM_PIXELS, pixel_order=PIXEL_ORDER, auto_write=False)

    print ("entre a main")
    
    listener()
