from pytube import YouTube
url=YouTube("https://www.youtube.com/watch?v=0gx46AlY758&list=RD54fea7wuV6s&index=6")
#you can change paste your preferred link above for the video that you want to downlaod
video = url.streams.first()
video.download()