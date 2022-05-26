from bs4 import BeautifulSoup
import requests
import os
import sys
import ctypes
import random
import webbrowser
import pathlib

COLS = 3
ROWS = 3 
searchQ = 'indian poverty varanasi'

if len(sys.argv) > 1:
	searchQ = sys.argv[1]
if len(sys.argv) > 2:
	COLS = sys.argv[2]
if len(sys.argv) > 3:
	ROWS = sys.argv[3]

user32 = ctypes.windll.user32
screenW, screenH = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

numberOfVideos = ROWS * COLS

resp = requests.get(f'https://www.youtube.com/results?search_query={searchQ}')

if resp.status_code != 200:
	print('Shit happens!')
	sys.exit(0)

bs = BeautifulSoup(resp.content, features='html.parser')
divVideos = bs.findAll('div', {'class':'yt-lockup-thumbnail contains-addto'})
videoUrls=[]
for v in divVideos:
	url = v.find('a').attrs['href'].split('=')[1]
	# print(url)
	videoUrls.append(url)

random.shuffle(videoUrls)

numberOfVideos = min(len(videoUrls), numberOfVideos)

HTML_TEMPLATE = '''
<!DOCTYPE html><html><body bgcolor='#000000'><style>body{overflow:hidden}</style>
	__divs__
	<script>
	  var tag = document.createElement('script');
	  tag.src = "https://www.youtube.com/iframe_api";
	  var firstScriptTag = document.getElementsByTagName('script')[0];
	  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
	  function onYouTubePlayerAPIReady()
	  {
		  __scripts__
	  }
      function onPlayerReady(event){setTimeout(event.target.playVideo, 500);}function onPlayerStateChange(event){if (event.data == YT.PlayerState.ENDED){event.target.playVideo();}}</script></body></html>
'''
videoW = (screenW-20)//ROWS
videoH = (screenH-30)//COLS

offsetY = 0
strPlayerDivs = ''
strPlayerScripts = ''
for i in range(0, numberOfVideos):
	currURL = videoUrls[i]
	strPlayerDivs += '<div id="ytplayer{0}"></div>'.format(i)
	strPlayerScripts += "new YT.Player('ytplayer{0}', {{width:'{1}', height: '{2}', videoId:'{3}', \
		playerVars: {{ 'autoplay': 1, 'loop':1, 'controls': 1, 'suggestedQuality':'small' }},	\
			events:{{'onStateChange': 'onPlayerStateChange'}}}});".format(i, videoW, videoH, currURL)

html = HTML_TEMPLATE.replace('__divs__', strPlayerDivs)
html = html.replace('__scripts__', strPlayerScripts)
with open('tmp.html', 'w') as f:
	f.write(html)


file_path = os.path.join(os.getcwd(), 'tmp.html')
file_path_uri = pathlib.Path(file_path).as_uri()
webbrowser.open(file_path_uri)





