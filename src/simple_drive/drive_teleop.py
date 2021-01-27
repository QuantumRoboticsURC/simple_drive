#!/usr/bin/python

import rospy
import subprocess

from sensor_msgs.msg import Joy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
from actionlib_msgs.msg import GoalID

class DriveTeleop:
    def __init__(self):
        self.speed_setting = 2 # default to medium speed

        #upper servo
        self.servo_pan_speed_u = rospy.get_param('~servo_pan_speed_u', 20) # degrees of change per button press
        self.servo_pan_max_u = rospy.get_param('~servo_pan_max_u', 160) # max angle of servo rotation
        self.servo_pan_min_u = rospy.get_param('~servo_pan_min_u', 0) # min angle of servo rotation
        self.servo_position_u = self.servo_pan_max_u/2 # center servo position

 	    #lower servo
        self.servo_pan_speed_l = rospy.get_param('~servo_pan_speed_l', 20) # degrees of change per button press
        self.servo_pan_max_l = rospy.get_param('~servo_pan_max_l', 160) # max angle of servo rotation
        self.servo_pan_min_l = rospy.get_param('~servo_pan_min_l', 0) # min angle of servo rotation
        self.servo_position_l = self.servo_pan_max_l/2 # center servo position

        #publisher
        self.cmd_vel_pub = rospy.Publisher("teleop/cmd_vel", Twist, queue_size=1)
        self.goal_cancel_pub = rospy.Publisher("move_base/cancel", GoalID, queue_size=1)
        self.servo_pub_u = rospy.Publisher("servo_pos_u", Float32, queue_size=1)
        self.servo_pub_l = rospy.Publisher("servo_pos_l", Float32, queue_size=1)
        self.joy_sub = rospy.Subscriber("joy", Joy, self.on_joy)

    def on_joy(self, data):
        # Set speed ratio using d-pad
        if data.axes[7] == 1: # full speed (d-pad up)
            self.speed_setting = 1
        if data.axes[6] != 0: # medium speed (d-pad left or right)
            self.speed_setting = 2
        if data.axes[7] == -1: # low speed (d-pad down)
            self.speed_setting = 3

        # Drive sticks
        left_speed = -data.axes[1] / self.speed_setting # left stick
        right_speed = -data.axes[5] / self.speed_setting # right stick

        # Convert skid steering speeds to twist speeds
        linear_vel  = (left_speed + right_speed) / 2.0 # (m/s)
        angular_vel  = (right_speed - left_speed) / 2.0 # (rad/s)

        # Publish Twist
        twist = Twist()
        twist.linear.x = linear_vel
        twist.angular.z = angular_vel
        self.cmd_vel_pub.publish(twist)

        # UPPER Servo camera control
        if data.buttons[1]: # up camera (X Button)
            if self.servo_position_u > self.servo_pan_min_u:
                self.servo_position_u -= self.servo_pan_speed_u
        if data.buttons[3]: # down camera (Triangle button)
            if self.servo_position_u < self.servo_pan_max_u:
                self.servo_position_u += self.servo_pan_speed_u
        if data.buttons[2]: # center servo position (Circle button)
            self.servo_position_u = self.servo_pan_max_u/2
        self.servo_pub_u.publish(self.servo_position_u)

        # LOWER Servo camera control
        if data.buttons[4]: # pan leftward (L1)
            if self.servo_position_l > self.servo_pan_min_l:
                self.servo_position_l -= self.servo_pan_speed_l
        if data.buttons[5]: # pan rightward (R1)
            if self.servo_position_l < self.servo_pan_max_l:
                self.servo_position_l += self.servo_pan_speed_l
        if data.buttons[0]: # center servo position (Square button)
            self.servo_position_l = self.servo_pan_max_l/2
        self.servo_pub_l.publish(self.servo_position_l)



        # Cancel move base goal
        if data.buttons[9]: # Options button
            rospy.loginfo('Cancelling move_base goal')
            cancel_msg = GoalID()
            self.goal_cancel_pub.publish(cancel_msg)

def main():
    rospy.init_node("drive_teleop")
    controller = DriveTeleop()
    rospy.spin()
