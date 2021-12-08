
from pytube import YouTube
import os

urls = ["https://youtube.com/example"]


def youtube_downloader(url):
    # Target to download at root directory/DownloadByProgram
    path = "./DownloadByProgram"

    # Mkdir
    if not os.path.isdir(path):
        os.mkdir(path)
    
    yt = YouTube(url)
    yt.streams.filter(subtype="mp4", progressive=True).first().download(path) # filter(res = "1080p")
    print("Downloaded One")

if __name__ == "__main__":
    for url in urls:
        youtube_downloader(url)
    print("Download Complete.")