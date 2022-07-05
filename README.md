# simple_drive

## Description

A simple robot drive system that includes skid steering joystick teleoperation, control of a panning two servos to look around the robot, and Arduino firmware.
This node only publishes the linear and angular velocity. The Closed Loop Velocity Control is made by this other [node](https://github.com/QuantumRoboticsURC/bus_can_drive).

##
![controller](https://raw.githubusercontent.com/QuantumRoboticsURC/simple_drive/main/images/simple_drive_controller.png)

## Quick Start

1. Install:

```
$ cd catkin/ws
$ git clone https://github.com/QuantumRoboticsURC/simple_drive.git
```

2. Launch ROS nodes:

```
$ roslaunch simple_drive drive_teleop.launch joy_dev:=/dev/input/js0
```
