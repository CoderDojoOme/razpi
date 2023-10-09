#!/usr/bin/env python
# -*- coding: utf-8 -*-
# video.py

import cv2

camera = cv2.VideoCapture(0) # 0 = Device ID

camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('Y','U','Y','V')) # YUYV = CODEC
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  # 320 640 800 1024
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240) # 240 480 600 576
camera.set(cv2.CAP_PROP_FPS, 3) # 24 frame rate N per sec

while True:
  ret, frame = camera.read()
  if not ret:
    break

  #frame4x = cv2.resize(frame, (1024,800))
  #cv2.imshow("Frame", cv2.flip(frame4x,0))
  # cv2flip 0:上下反転 1:左右反転 -1:上下左右反転
  cv2.imshow("Frame", cv2.flip(frame,0))
  key = cv2.waitKey(1)

  # Escキーを入力されたら画面を閉じる
  if key == 27:
    break

camera.release()
cv2.destroyAllWindows()
