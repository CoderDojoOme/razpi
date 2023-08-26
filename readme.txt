■■■■■■■■■■■■■■■■■■■■■■■■■
■ CoderDojo青梅　2023年８月版 Rev.02
■■■■■■■■■■■■■■■■■■■■■■■

このファイル郡は razpi10.local からpushされています

// -------------------------------------------------------------------------------
// その１．音楽プレイヤー「omxplayer」RaspberryPi用軽量メディアプレーヤー(mp3音楽, mp4動画)
// -------------------------------------------------------------------------------

　※ ラズパイのイヤホンジャックにヘッドホンやイヤホンを接続します

【１】インストール済みだが、無ければインストールする　$ sudo apt install omxplayer -y

【２】音楽を鳴らすコマンド
　使い方：コマンドラインで音楽ファイルを鳴らすメディアプレーヤー。Linuxでコマンドを実行します（pythonではありません）。
　　$ omxplayer music.mp3 -o local --vol -500
　オプションの[-o]は[local]の時がイヤホンジャック出力で、[hdmi]の時がディスプレイのスピーカー出力です。

【３】インターネットからWEBサイトのファイルをダウンロードするコマンド
　$ wget <URL>

【４】（無料BGM素材：甘茶の音楽工房）
　
　▼ダークテクノ「メトロポリス」
　https://amachamusic.chagasi.com/mp3/metropolis.mp3
　
　▼テクノ・エレクトロ「ピコピコディスコ」
　https://amachamusic.chagasi.com/mp3/picopicodisco.mp3
　
　▼テクノ・エレクトロ「レトロパーク」
　https://amachamusic.chagasi.com/mp3/retropark.mp3
　
　▼ファンタジー「フィヨルドの澄んだ風」
　https://amachamusic.chagasi.com/mp3/fjordnosundakaze.mp3

// -------------------------------------------------------------------------------
// その２．音声合成AI「Open JTalk」
// -------------------------------------------------------------------------------
日本の大学で開発された音声合成AI技術。テキストを音声に変換

【１】使い方：ダブルコーテーションで囲った日本語を読み上げます。
　$ ./jtalk.sh　“がんばれ。みんな”

【２】[jtalk.sh]は、プログラムコードです。ファイルの中を見てみましょう。
　$ cat jtalk.sh

// ----------------- ここからjtalk.shのコード --------↓↓↓↓↓↓↓
#!/bin/bash
# ファイル名:jtalk.sh
# ファイルを指定
# chmod +x jtalk.sh # 実行権限をつけること
voice=/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice
dic=/var/lib/mecab/dic/open-jtalk/naist-jdic

# パラメータを定義
option="-m $voice \
  -s 30000 \
  -p 150 \
  -a 0.03 \
  -u 0.0 \
  -jm 1.0 \
  -jf 1.0 \
  -x $dic \
  -ow output.wav"

# テキストを音声データに変換実行
echo "$1" | open_jtalk $option

// -------------------------------------------------------------------------------
// その３．音楽プレーヤー　［aplay］
// -------------------------------------------------------------------------------

# 音声をスピーカーで鳴らす。
aplay -q -D hw:0,0 output.wav
// ----------------- ここまでjtalk.shのコード --------↑↑↑↑↑↑↑↑

【３】使い方：［aplay］で音声wavファイルを鳴らす。鳴らないときはデバイス番号が違うかも
　$ aplay  -q  -D  hw:0,0  output.wav

【４】使い方：［aplay］でデバイス番号を調べる
　$ aplay  -l
　　**** ハードウェアデバイス PLAYBACK のリスト ****
　　カード 0: Headphones [bcm2835 Headphones], デバイス 0: bcm2835 Headphones [bcm2835 Headphones]  
　　　サブデバイス: 8/8
  　　サブデバイス #0: subdevice #0
  　　サブデバイス #1: subdevice #1

// -------------------------------------------------------------------------------
// その４．［Open JTalk］「めいちゃんの声」に変えてみます
// -------------------------------------------------------------------------------

【１】使い方：「jtalk.sh」でなく　「jtalk_mei.sh」
　$ ./jtalk_mei.sh "めいちゃんの声です“, “normal”
　$ ./jtalk_mei.sh "めいちゃんの声です“, “angry”
　$ ./jtalk_mei.sh "めいちゃんの声です“, “happy”
　$ ./jtalk_mei.sh "めいちゃんの声です“, “sad”

// -------------------------------------------------------------------------------
// その５．百科事典　Wikipedia検索
// -------------------------------------------------------------------------------

【１】コードを作ります（インターネットのWikipediaで単語を調べるプログラム）

　1. 新しいファイルを作成する　$ nano wiki.py
　2. 講師がコードを書きます
　3. 作ったプログラムを実行する　$ python wiki.py

// -------------------------------------------------------------------------------
// その６．サーボモーター
// -------------------------------------------------------------------------------

【１】使い方：サーボモーターの動作テスト
　　$ python   servo.py
　　動作真ん中（7.0）が初期値　→　左（12.0）に移動　→　右（2.0）に移動する

【２】使い方：左右に少しずつ、ずーっと繰り返す
　　$ python   servo1.py

【３】使い方：キーボード操作で動かす
　　$ python   servo2.py

　　キー操作：
　　[a]90 [s]++ [d]0 [f]-- [g]-90  [q]end




// -------------------------- 以下は無視してください ------------------------------------------------


■Raspberry Pi 3 B+, Raspberry Pi は９年間 旧Raspbianを2年ごとにアップデートしてきた。
　2022年5月新Raspberry Pi OS は２種類リリースされる。
　Raspberry Pi OS,        Debian Bullseye
　Raspberry Pi OS Legacy, Debian Buster

・Jessie (Debian 8系)　ラピロ搭載時のOSバージョン 2015
　　↓
・Stretch (Debian 9系)　2017-
　　↓
・Buster（Debian 10系）2019-2024年6月まで, Linuxカーネル5.10は2026年12月までサポートされる。
・Bullseye（Debian 11系）2021-
　　↓
・（予定）Bookworm

　$ cat /etc/os-release
　PRETTY_NAME="Raspbian GNU/Linux 10 (buster)"
　$ uname -r
　5.10.103-v7+


パッケージが壊れてないかなどを念のためチェック
dpkg -C

cat etc/*release
sudo apt clean


--------------------
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

  #frame2x = cv2.resize(frame, (640,480))
  cv2.imshow("Frame", cv2.flip(frame,0))
  key = cv2.waitKey(1)

  # Escキーを入力されたら画面を閉じる
  if key == 27:
    break

camera.release()
cv2.destroyAllWindows()

------------------------------------------------------------------

pin 4- 8 ショート; PWM Duty 効かない, しかし100%速度で全て動く
pin 4- 8 オープン; PWM Duty 効く, しかし50%速度の時、回転しない場合がある
pin 4- 8 オープン; PWM Duty 効く, 1000Hzなら50%速度の時も全て動く




