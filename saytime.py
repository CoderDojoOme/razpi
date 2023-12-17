#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime

cmd = "./jtalk.sh '只今の時刻は、" + str(datetime.datetime.today().hour) + "時"  + str(datetime.datetime.today().minute) + "分です。'"
print(cmd)
os.system(cmd)

