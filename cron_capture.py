#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ファイル名: capture.py
import cv2
import os
import datetime

if __name__=="__main__":
    # Haar-like特徴分類器ファイルの読み込み。ファイルの場所は自分の環境に合わせてください。

    # [cv2.data.haarcascades]ディレクトリにxmlファイルがある
    cascade_path = os.path.join( cv2.data.haarcascades, "haarcascade_frontalface_default.xml")
    face_cascade = cv2.CascadeClassifier(cascade_path)

    # USBカメラで画像を取得する。
    capture = cv2.VideoCapture(0)
    rtn, frame = capture.read()
    if( rtn == True ):
        cv2.imwrite( "capture.jpg", frame )

    # 画像ファイルをグレースケールに変換する。
    frame = cv2.rotate( frame, cv2.ROTATE_180 )
    gray = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY )

    # 顔を検知する。
    faces = face_cascade.detectMultiScale( gray )

    for rect in faces:
        # 検知した顔を四角で囲む（rect[*]:0=x, 1=y, 2=width, 3=height）。
        color = (0,255,0)    # 緑色(BGR)。
        thickness = 2
        cv2.rectangle( frame, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), color, thickness )
        #cv2.arrowedLine( frame, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), color, thickness )

    # 画像ファイルを保存する。
    now = datetime.datetime.now()
    filename = "/home/pi/python/pic/pic{0:%Y%m%d_%H%M%S}.jpg".format(now)
    cv2.imwrite( filename, frame )

    # 終了処理（ストリームを解放）
    capture.release()
    cv2.destroyAllWindows()
