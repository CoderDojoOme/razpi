#!/usr/bin/env python
# -*- coding: utf-8 -*-

# sudo pip install readchar

import RPi.GPIO as GPIO
import sys
import time
import readchar

constLeftIN1 = 27 #GPIO No.
constLeftIN2 = 22 #GPIO No.
constRightIN1 = 20 #GPIO No.
constRightIN2 = 21 #GPIO No.

GPIO.setwarnings( False )
GPIO.setmode( GPIO.BCM )
GPIO.setup( constLeftIN1,  GPIO.OUT )
GPIO.setup( constLeftIN2,  GPIO.OUT )
GPIO.setup( constRightIN1, GPIO.OUT )
GPIO.setup( constRightIN2, GPIO.OUT )


def moveForward():
	GPIO.output( constLeftIN1, 1 )
	GPIO.output( constLeftIN2, 0 )
	GPIO.output( constRightIN1, 1 )
	GPIO.output( constRightIN2, 0 )

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
	GPIO.cleanup()
	sys.exit(0)

######################################
# メインルーチン
######################################
if __name__ == '__main__':

	print('   [W]\n[A][S][D]\n[X] to STOP\n[Q] to QUIT')

	try:
		while True:
			kb = readchar.readchar()
			sys.stdout.write(kb)

			if kb == 'w':
				moveForward()
			if kb == 's':
				moveBack()
			if kb == 'a':
				moveLeft()
			if kb == 'd':
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
