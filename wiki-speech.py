#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wiki-speech.py

import wikipedia
import sys
import os

# Wikiの検索
def main_wiki( strText ):
	# 単語のサマリーを取得。
	print( strText + "ですね。ちょっとお待ちください。" )
	wikipedia.set_lang("ja")
	#print wikipedia.summary( strText )
	try:
		strReturn = wikipedia.summary( strText, sentences=1 ).encode("utf-8")
	except:
		print( "いっぱい考えたけど、思い出せなかっです。" )
	finally:
		print( strReturn.decode('utf-8') )
		strReturn = strReturn.decode('utf-8') + "の事です。"
		strCMD = "./jtalk.sh '" + strReturn + "' 'normal'"
		os.system( strCMD )

	# タイトルの取得。
	print( "▼タイトル" )
	ny = wikipedia.page( strText )
	print( ny.title )

	# 単語の詳細情報を取得。
	print( "▼詳細情報" )
	print( ny.content )
        #とても口語で喋るには情報量が多すぎるのでコメントアウト。

# 初期設定
if __name__ == '__main__':
	if (len(sys.argv) <= 1):
		print("Syntax: python wiki-speech.py '[text]'")
		sys.exit()
	else:
		main_wiki( sys.argv[1] )

