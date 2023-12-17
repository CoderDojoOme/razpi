<<<<<<< HEAD
=======
$ cat video-sonic.py 
>>>>>>> 535e72fda6008108e0ece790676f9a59ad67ee1b
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys
import cv2
from timeout_decorator import timeout

# 初期設定 of カメラ
camera = cv2.VideoCapture(0) # 0 = Device ID
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('Y','U','Y','V')) # YUYV = CODEC
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 320 640 800 1024
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 240 480 600 576
camera.set(cv2.CAP_PROP_FPS, 3) # 24 frame rate N per sec

# 初期設定 of 超音波センサー
TRIG_PIN = 23
ECHO_PIN = 24
SoundSpeed = 34000   # 音速(cm/s)
GPIO.setmode(GPIO.BCM)     # GPIO BCMモードに設定
GPIO.setwarnings(False)    # GPIO警告無効化
GPIO.setup( TRIG_PIN, GPIO.OUT )
GPIO.setup( ECHO_PIN, GPIO.IN  )

# 初期設定 of 図形 RGBは'BGR'の順
colorRed = (0,0,178)
colorYellow = (0,215,255)
colorGreen = (50,205,50)
graphPosition = (10,20)
fontSize = 0.5
fontColor = (255,255,0) #水色

######################################
# メインルーチン
######################################
def main():
  while True:
    try:
      ret, frame = camera.read()
      if not ret:
        break

      # 画像に図形を追加する
      imgFrame = cv2.flip(frame,-1)
      intDistance = measure()
      #print( strDistance )
<<<<<<< HEAD
      tmpColor = (10,10,10)
=======
>>>>>>> 535e72fda6008108e0ece790676f9a59ad67ee1b
      if ( intDistance < 7 ):
        tmpColor = colorRed
      elif ( intDistance < 20 ):
        tmpColor = colorYellow
      else:
        tmpColor = colorGreen
      # 距離
      intLength = 1
<<<<<<< HEAD
      if ( intDistance > 50 or intDistance < 0 ):
=======
      if ( intDistance > 50 ):
>>>>>>> 535e72fda6008108e0ece790676f9a59ad67ee1b
        intLength = 50
      else:
        intLength = intDistance
      # rectangle( image, 左上座標, 右下座標, 色, 線の太さ[負は塗りつぶし])
      cv2.rectangle( imgFrame, graphPosition, ( 10 + intLength * 10, 30 ), tmpColor, -1 )
      # putText( image, text, location, font, fontScale, color)
<<<<<<< HEAD
      cv2.putText( imgFrame, str(intDistance) + " cm", (30,50), cv2.FONT_HERSHEY_SIMPLEX, fontSize, fontColor)
=======
      cv2.putText( imgFrame, str(intDistance), (30,50), cv2.FONT_HERSHEY_SIMPLEX, fontSize, fontColor)
>>>>>>> 535e72fda6008108e0ece790676f9a59ad67ee1b

      # 動画画像を表示する
      # frame4x = cv2.resize(frame, (1024,800))
      # cv2.imshow("Frame", cv2.flip(frame4x,0))
      # cv2flip 0:上下反転 1:左右反転 -1:上下左右反転
      cv2.imshow("Frame", imgFrame)
      key = cv2.waitKey(1)

<<<<<<< HEAD
    except TypeError:
      print( intLength )
      print( tmpColor )
      print( graphPosition )
      print( 'タイプエラー：たぶん' )

=======
>>>>>>> 535e72fda6008108e0ece790676f9a59ad67ee1b
    except TimeoutError:
      print( '計測タイムアウト' )

    except KeyboardInterrupt:
      camera.release()
      cv2.destroyAllWindows()
      GPIO.cleanup()
      sys.exit()

    # Escキーを入力されたら画面を閉じる
    # if key == 27:
    #   sys.exit()

@timeout(5) # measure()関数のタイムアウト時間を設定する
def measure():
    sigon = sigoff = 0
    # 10μsだけ超音波をHighにして計測する
    GPIO.output( TRIG_PIN, GPIO.HIGH )
    time.sleep( 0.00001 )
    GPIO.output( TRIG_PIN, GPIO.LOW )

    try:
      while( GPIO.input( ECHO_PIN ) == GPIO.LOW ):
          sigoff = time.time()
      while( GPIO.input( ECHO_PIN ) == 1 ):
          sigon = time.time()
      intTemp = int( round((( sigon - sigoff ) * SoundSpeed) / 2 ) )  # + "cm"
      return( intTemp )
    
    except:
      print('measure()関数内でタイムアウト発生')
      return( 999 )

if __name__ == '__main__':
    time.sleep(1.0)
    main()
