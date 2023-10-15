#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

TRIG_PIN = 23
ECHO_PIN = 24
SoundSpeed = 34000   # 音速(cm/s)

GPIO.setmode(GPIO.BCM)     # GPIO BCMモードに設定
GPIO.setwarnings(False)    # GPIO警告無効化
GPIO.setup( TRIG_PIN, GPIO.OUT )
GPIO.setup( ECHO_PIN, GPIO.IN  )

def main():
    print( "run Sonic" )
    while True:
        try:
            strDistance = measure()
            print( strDistance )
            time.sleep(1.0)
        except KeyboardInterrupt:
            GPIO.cleanup()
            sys.exit()

def measure():
    sigon = sigoff = 1
    # 10μsだけ超音波をHighにして計測する
    GPIO.output( TRIG_PIN, GPIO.HIGH )
    time.sleep( 0.00001 )
    GPIO.output( TRIG_PIN, GPIO.LOW )

    while( GPIO.input( ECHO_PIN ) == GPIO.LOW ):
        sigoff = time.time()
    while( GPIO.input( ECHO_PIN ) == 1 ):
        sigon = time.time()
    strTemp = str( round((( sigon - sigoff ) * SoundSpeed) / 2 ) ) + "cm"
    return( strTemp )

if __name__ == '__main__':
    main()


