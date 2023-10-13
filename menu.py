cat menu.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

RUNNING = True

try:
  while RUNNING:
    print (u'--- 機能一覧 ---')
    print (u'[c] ラズパイカメラ画像を表示 ※リモートデスクトップ必須, video.py')
    print (u'[d] ラズタンク・キー操作［TB6612FNG］, tank4_c-type.py')
    print (u'[e] ラズタンク・キー操作［ノーマルTA7721P］, tank.py')
    print (u'[f] サーボモーター［GPIO14］, servo2.py')
    print (u'[g] 超音波センサー, sonic.py')
    print (u'[h] 音声合成[時刻お知らせ], saytime.py')
    print (u'[0] End')

    inputWord = input('>>>  ')

    #print ('*** debug *** [' + str(inputWord) + '] was selected.')

    if inputWord == 'c':
        os.system( "python video.py" )

    if inputWord == 'd':
        os.system( "python tank4_c-type.py" )

    if inputWord == 'e':
        os.system( "python tank4.py" )

    if inputWord == 'f':
        os.system( "python servo2.py" )

    if inputWord == 'g':
        os.system( "python sonic.py" )

    if inputWord == 'h':
        os.system( "python saytime.py" )

    elif inputWord == '0':
        break

    else:
        print('No function executed.')

except KeyboardInterrupt:
  RUNNING = False

finally:
  print('See you,')
