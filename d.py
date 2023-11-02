# from pytube import YouTube
# #YouTube("https://www.youtube.com/watch?v=FSR1s2b-l_I&list=PLTCrU9sGyburBw9wNOHebv9SjlE4Elv5a&index=1").streams.first().download()
# yt = YouTube('https://www.youtube.com/watch?v=FSR1s2b-l_I&list=PLTCrU9sGyburBw9wNOHebv9SjlE4Elv5a&index=1')
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()



#tested
# from pytube import Playlist 

# playlist = Playlist('https://www.youtube.com/watch?v=0WST5mM-ug4')

# for video in playlist.videos:
#     print('downloading : {} with url : {}'.format(video.title, video.watch_url))
#     video.streams.\
#         filter(type='video', progressive=True, file_extension='mp4').\
#         order_by('resolution').\
#         desc().\
#         first().\
#         download("D:")
from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)