#!/usr/bin/env python
# -*- coding: utf-8 -*-
# servo.py
import RPi.GPIO as GPIO
import time

contPIN = 23
GPIO.setmode( GPIO.BCM )
GPIO.setup( contPIN, GPIO.OUT )
servo = GPIO.PWM( contPIN, 50 )  #50Hz
servo.start( 0.0 )

servo.ChangeDutyCycle( 7.0 ) # angle
time.sleep(1.0)
servo.ChangeDutyCycle( 12.0 ) # angle
time.sleep(1.0)
servo.ChangeDutyCycle( 2.0 ) # to be stable
time.sleep(1.0)
servo.ChangeDutyCycle( 7.0 ) # to be stable
time.sleep(1.0)

servo.stop()
GPIO.cleanup()

