#include <Arduino.h>
#include <Servo.h>

// Pin to the Servo
#define pinServo1 5
#define pinServo2 6

Servo theServo1; // the servo used to control a camera that can look around the robot
Servo theServo2;

struct DATA {
    float servo_U;
    float servo_L;
} received;



void setup() {
    Serial.begin(9600);
    theServo1.attach(pinServo1);
    theServo2.attach(pinServo2);
}

void loop() {
       if (cmd == 2) {
           Serial.readBytes((char *) &received.servo_U, sizeof(float));
           theServo1.write((int) received.servo_U);
       }
       else if (cmd == 4) {
           Serial.readBytes((char *) &received.servo_L, sizeof(float));
           theServo2.write((int) received.servo_L);
       }
   }
}

