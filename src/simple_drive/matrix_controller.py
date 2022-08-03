#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64, Int32
import time

# Matrix
import board
import neopixel_spi as neopixel

def on_new_led(data):    
    global state
    state = data.data
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
    else:
        for i in range(64):
            pixels[i] = COLORS[data.data]
    pixels.show()

def change_color(color):
    for i in range(64):
        pixels[i] = COLORS[color]
    pixels.show()
    
def listener():
    rospy.init_node('matrix_controller', anonymous=True)
    subscriber_led = rospy.Subscriber("status_led", Int32, on_new_led, queue_size = 10)
    green = False

    """while True:
        if state == 3:
            if green:
                change_color(0)
            else:
                change_color(3)
            green = not green
        else:
            change_color(state)
        #time.sleep(.5)"""
    rospy.spin()

if __name__ == '__main__':
    NUM_PIXELS = 64
    PIXEL_ORDER = neopixel.RGB    
    COLORS = (0x000000, 0x0000FF, 0x00FF00, 0xFF0000)
    #Green RED Blue aunque arriba diga RGB XD, esta en bgr pero si lo invierno se vuelve a invertir todo
    spi = board.SPI()
    pixels = neopixel.NeoPixel_SPI(spi, NUM_PIXELS, pixel_order=PIXEL_ORDER, auto_write=False)
    state = 0

    listener()
