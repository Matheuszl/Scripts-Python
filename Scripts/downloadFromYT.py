import pytube

cipher = "https://www.youtube.com/watch?v=Nt01A2fmA0c"

video = pytube.YouTube(cipher)
youtube = video.streams.first()
youtube.download(r'C:\Users\matza\Desktop')

print("Download true")