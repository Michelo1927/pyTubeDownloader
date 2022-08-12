from pytube import YouTube
from sys import argv

link = argv[1]
type = argv[2]
yt = YouTube(link)

print("Downloading now: "+ "\n" + yt.title)
#res = yt.streams.filter(file_extension='mp4')
if type == "audio":
    #audio only
    stream = yt.streams.get_audio_only()

elif type == "video":
    #max resolution
    stream = yt.streams.get_highest_resolution()

#elif type == "1080":
    #full hd
    #stream = yt.streams.filter(res="1080p")





stream.download('')






