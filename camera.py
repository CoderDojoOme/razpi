#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import picamera
import time

def capture( intW, intH ):
    global picamera
    picamera = picamera.PiCamera()
    picamera.resolution = (intW, intH)
    picamera.rotation = 180
    picamera.start_preview()
    picamera.led = True
    #time.sleep(2)
    picamera.capture( "/home/pi/python/picture.jpg" )

if __name__ == '__main__':
    if (len(sys.argv) <=2):
        intWidth = 800
        intHeight = 600
    else:
        intWidth = int(sys.argv[1])
        intHeight = int(sys.argv[2])

    capture( intWidth, intHeight )

