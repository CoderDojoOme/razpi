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

# 音声をスピーカーで鳴らす。
aplay -q -D hw:0,0 output.wav
