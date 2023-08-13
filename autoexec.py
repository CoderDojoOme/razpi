#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This will called from /etc/rc.local
import os

if __name__ == '__main__':

    cmd = "aplay -D hw:1,0 /home/pi/Music/s-pipi.wav"
    os.system( cmd )
