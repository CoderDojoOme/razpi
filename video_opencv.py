#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import os

# カメラデバイスを指定する（0 = Device ID）
camera = cv2.VideoCapture(0) 

camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('Y','U','Y','V')) # YUYV = CODEC
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 800)  # 320 640 800 1024
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 600) # 240 480 600 576
camera.set(cv2.CAP_PROP_FPS, 3) # 24 frame rate N per sec

# Haar-like特徴分類器ファイルの読み込み。ファイルの場所は自分の環境に合わせてください。
# [cv2.data.haarcascades]ディレクトリにxmlファイルがある
cascade_path = os.path.join( cv2.data.haarcascades, "haarcascade_frontalface_default.xml")
face_cascade = cv2.CascadeClassifier(cascade_path)

while True:
  # カメラ画像取得
  ret, frame = camera.read()
  if not ret:
    break

  #cv2.flip（第一引数は画像データ, 第二引数が方向［0:上下反転, 1:左右反転, -1:左右反転&上下反転］）
  imgFlip = cv2.flip(frame,0)
  # 画像ファイルをグレースケールに変換する。
  gray = cv2.cvtColor( imgFlip, cv2.COLOR_BGR2GRAY )
  # 顔を検知する。
  faces = face_cascade.detectMultiScale( gray )
  # 検知した顔を四角で囲む（rect[*]:0=x, 1=y, 2=width, 3=height）。
  for rect in faces:
    color = (0,255,0)    # 緑色(BGR)。
    thickness = 2
    cv2.rectangle( imgFlip, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), color, thickness )

  #frame4x = cv2.resize(frame, (1024,800))
  #cv2.imshow("Frame", cv2.flip(frame4x,0))
  #cv2.imshow（第一引数はウィンドウのタイトル名, 第二引数が画像データ）
  cv2.imshow("Frame", imgFlip)
  # waitKey（キー入力を待つ時間 ミリ秒）
  key = cv2.waitKey(1)

  # Escキーを入力されたら画面を閉じる
  if key == 27:
    break

camera.release()
cv2.destroyAllWindows()
