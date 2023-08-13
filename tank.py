#!/usr/bin/env python
# -*- coding: utf-8 -*-

# sudo pip install readchar

import RPi.GPIO as GPIO
import sys
import time
import readchar

constLeftPWM = 17
constLeftIN1 = 27
constLeftIN2 = 22
constRightPWM = 16
constRightIN1 = 20
constRightIN2 = 21

GPIO.setwarnings( False )
GPIO.setmode( GPIO.BCM )
GPIO.setup( constLeftPWM,  GPIO.OUT )
GPIO.setup( constLeftIN1,  GPIO.OUT )
GPIO.setup( constLeftIN2,  GPIO.OUT )
GPIO.setup( constRightPWM, GPIO.OUT )
GPIO.setup( constRightIN1, GPIO.OUT )
GPIO.setup( constRightIN2, GPIO.OUT )

pwmLeft = GPIO.PWM( constLeftPWM, 50 )  #50Hz
pwmLeft.start( 0.0 )
pwmRight = GPIO.PWM( constRightPWM, 50 )  #50Hz
pwmRight.start( 0.0 )

def moveForward():
	GPIO.output( constLeftIN1, 1 )
	GPIO.output( constLeftIN2, 0 )
	GPIO.output( constRightIN1, 1 )
	GPIO.output( constRightIN2, 0 )

def speedSlow():
	pwmLeft.ChangeDutyCycle( 80 )
	pwmRight.ChangeDutyCycle( 80 )

def speedHigh():
	pwmLeft.ChangeDutyCycle( 100 )
	pwmRight.ChangeDutyCycle( 100 )

def moveBack():
	GPIO.output( constLeftIN1, 0 )
	GPIO.output( constLeftIN2, 1 )
	GPIO.output( constRightIN1, 0 )
	GPIO.output( constRightIN2, 1 )

def moveLeft():
	GPIO.output( constLeftIN1, 0 )
	GPIO.output( constLeftIN2, 1 )
	GPIO.output( constRightIN1, 1 )
	GPIO.output( constRightIN2, 0 )

def moveRight():
	GPIO.output( constLeftIN1, 1 )
	GPIO.output( constLeftIN2, 0 )
	GPIO.output( constRightIN1, 0 )
	GPIO.output( constRightIN2, 1 )

def moveStop():
	GPIO.output( constLeftIN1, 0 )
	GPIO.output( constLeftIN2, 0 )
	GPIO.output( constRightIN1, 0 )
	GPIO.output( constRightIN2, 0 )

def end():
	pwmLeft.stop()
	pwmRight.stop()
	GPIO.cleanup()
	sys.exit(0)

######################################
# メインルーチン
######################################
if __name__ == '__main__':

	try:
		while True:
			kb = readchar.readchar()
			sys.stdout.write(kb)

			if kb == 'w':
				speedHigh()
				moveForward()
			if kb == 'z':
				speedHigh()
				moveBack()
			if kb == 'a':
				speedHigh()
				moveLeft()
			if kb == 's':
				speedHigh()
				moveRight()
			if kb == 'x':
				moveStop()
			if kb == 'q':
				end()
			#time.sleep(0.2)
			#moveStop()

	except KeyboardInterrupt:
		moveStop()
		end()

