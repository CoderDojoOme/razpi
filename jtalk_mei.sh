#!/bin/bash
# ファイル名:jtalk.sh
# ファイルを指定
# ↓最初にインストールした男性の声
#voice=/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice
# ↓追加した女性の声（メイちゃん）
if [ $2 == "normal" ]; then
  voice=/usr/share/hts-voice/mei/mei_normal.htsvoice
elif [ $2 == "angry" ]; then
  voice=/usr/share/hts-voice/mei/mei_angry.htsvoice
elif [ $2 == "happy" ]; then
  voice=/usr/share/hts-voice/mei/mei_happy.htsvoice
elif [ $2 == "sad" ]; then
  voice=/usr/share/hts-voice/mei/mei_sad.htsvoice
else
  voice=/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice
fi

# ↓辞書ファイルのあるディレクトリ
dic=/var/lib/mecab/dic/open-jtalk/naist-jdic

# パラメータを定義
option="-m $voice \
  -s 48000 \
  -p 240 \
  -a 0.5 \
  -u 0.0 \
  -jm 1.0 \
  -jf 1.0 \
  -x $dic \
  -ow output.wav"

# テキストを音声データに変換実行
echo "$1" | open_jtalk $option

# 音声をスピーカーで鳴らす。
aplay -q -D hw:0,0 output.wav
