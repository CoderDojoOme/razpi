#coding=utf-8

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode ( GPIO.BCM )
GPIO.setup ( 18, GPIO.OUT)
pi = GPIO.PWM ( 18, 30 )  #( pin, Hz ) 30Hz for MS18
pi.start ( 0 )
pi.ChangeDutyCycle( 0 )

try:
    while True:
        for i in range(0, 10):
            duty = i
            print(duty)
            pi.ChangeDutyCycle( duty )
            sleep(0.5)
        for i in range(0, 10):
            duty = 10 - i
            print(duty)
            pi.ChangeDutyCycle( duty )
            sleep(0.5)

except KeyboardInterrupt:
    pass
pi.stop()
GPIO.cleanup()

