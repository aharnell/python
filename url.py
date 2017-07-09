#!python
import urllib.request
url = "http://uproxx.com/tv/best-shows-on-netflix-good-tv-series-ranked/"
with urllib.request.urlopen(url) as text:
	for line in text.readlines():
		print(line.decode('utf-8'))