# simple_drive

## Description

A simple robot drive system that includes skid steering joystick teleoperation, control of a panning two servos to look around the robot, and Arduino firmware.

##
![controller](https://raw.githubusercontent.com/QuantumRoboticsURC/simple_drive/main/images/drive_system_PS5_Controller.png)

## Quick Start

1. Install:

```
$ cd catkin/ws
$ git clone https://github.com/QuantumRoboticsURC/simple_drive.git
```

2. Launch ROS nodes:

```
$ roslaunch simple_drive drive_teleop.launch joy_dev:=/dev/input/js1
$ roslaunch simple_drive cmd_vel_mux.launch
$ roslaunch simple_drive simple_drive.launch serial_dev:=/dev/ttyUSB0
```

3. Install the drive_firmware onto a microcontroller connected to motors and wheels.

```
$ 

```

4. Install the Servo library and run the code

```
$ roscd simple_drive
$ cd ./drive_firmware/
$ pio init --board uno
$ pio lib install "arduino-libraries/Servo@^1.1.7"
$ pio run --target upload
```

5. The cu command is used to call up another syste  and act as a dial in terminal

```
$ sudo apt-get install cu
$ cu -l /dev/ttyACM0 -s 115200

```

