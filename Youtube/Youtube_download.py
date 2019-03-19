import requests
from pytube import YouTube
import re
import os

videooutList = []

#urltext='/watch?v=Ew4VvF0DPMc&list=RDEw4VvF0DPMc&start_radio=1&t=175&t=176'
#url='https://www.youtube.com'+urltext
url_input=input("請輸入播放清單中的影片網址:")
url=url_input

pathdir='download'
if not os.path.isdir(pathdir):
        os.mkdir(pathdir)
html = requests.get(url)
resl = re.findall(r'/watch[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%?=~_|]',html.text)
for temurl in resl:
    if 'list='and 'index='in temurl:
        if temurl not in videooutList:
            videooutList.append(temurl)

print('開始下載')
n=1
for video in videooutList:
    yt=YouTube('https://www.youtube.com'+video)
    print(str(n)+'. '+yt.title)
    yt.streams.filter(subtype='mp4',res='360p',progressive=True).first().download(pathdir)
    n=n+1
print('下載完成，檔案存於'+pathdir)

