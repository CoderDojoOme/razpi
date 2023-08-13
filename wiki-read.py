import wikipedia

wikipedia.set_lang("ja")
result = wikipedia.page("ホバークラフト")
print(result.summary)

