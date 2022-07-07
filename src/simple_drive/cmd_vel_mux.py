#!/usr/bin/python

import rospy
import time

from std_msgs.msg import *
from geometry_msgs.msg import Twist
#variable de decision
objeto = 0

def detectobjeto(flag):
    global objeto
    objeto = int(flag.data)
    pub2.publish(str(type(objeto)))

def on_autonomous_cmd(twist):
    time_since_human_cmd = time.time() - human_cmd_time
    if time_since_human_cmd >= block_duration:
        block_duration = 0 # stop blocking
        pub.publish(twist)

def on_human_cmd(twist): #Esta funcion transforma el decision auto
    global objeto
    human_cmd_time = time.time()
    block_duration = rospy.get_param('~block_duration', 5) # to get the lowest latency, comment this or hard code this so that there is no call to rospy.get_param
    #pub.publish(twist)
    #TOMA LA DECISION DE OBEDECER O PARAR        
    if(objeto == 0):
        pub.publish(twist)
        mtri.publish(0)
    elif(objeto == 1):
        twist0 = Twist()
        twist0.linear.x = 0
        twist0.angular.z = 0
        pub.publish(twist0)
        mtri.publish(1)


pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
pub2 = rospy.Publisher("val", String, queue_size=10)
mtri = rospy.Publisher('/matrix',Int64,queue_size = 10)
def main():
    rospy.init_node("cmd_vel_mux")
    
    ## TOPICO QUE AYUDA A SABER SI HAY DETECCION Y EN CASO AFIRMATIVO, CAMBIAR LA VARIABLE GLOBAL
    rospy.Subscriber("detection",String, detectobjeto)
    #rospy.Subscriber("move_base/cmd_vel", Twist, on_autonomous_cmd)
    rospy.Subscriber("teleop/cmd_vel", Twist, on_human_cmd)
    block_duration = 0
    human_cmd_time = time.time()
    rospy.spin()

