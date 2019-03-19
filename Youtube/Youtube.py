from pytube import YouTube
import os
url_input=input("請輸入影片網址:")
yt = YouTube(url_input)
print('開始下載:'+yt.title)
pathdir='d:\\tem1'
if not os.path.isdir(pathdir):
        os.mkdir(pathdir)
yt.streams.first().download(pathdir)
print('『'+yt.title+'』下載完成，檔案存於'+pathdir)
