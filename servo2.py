#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import sys
import readchar

contPIN = 18
GPIO.setmode( GPIO.BCM )
GPIO.setup( contPIN, GPIO.OUT )
servo = GPIO.PWM( contPIN, 50 )  #50Hz
servo.start( 0.0 )

angle = 0.0
print( "[a]90 [s]++ [d]0 [f]-- [g]-90  [q]end" )

def end():
  servo.stop()
  GPIO.cleanup()
  sys.exit(0)

def move( angle ):
  angle = round( angle, 1 )
  print( angle )
  duty = 2.5 + (12.0-2.5) * (angle+90) /180
  servo.ChangeDutyCycle( duty )

while True:
  kb = readchar.readchar()

  if kb == 'a':
    angle = 90
    move( angle )

  if kb == 's':
    angle += 1
    if angle > 90:
      angle = 90
    move( angle )

  if kb == 'd':
    angle = 0
    move( angle )

  if kb == 'f':
    angle -= 1
    if angle < -90:
      angle = -90
    move( angle )

  if kb == 'g':
    angle = -90
    move( angle )

  if kb == 'q':
    end()


