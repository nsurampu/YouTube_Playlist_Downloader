from pytube import YouTube
import urllib
import lxml.html
import pafy

print("\n***YouTube Playlist Downloader***\n")
text_file = open("filePath.txt", "r+") # Opens the file "filePath.txt"
text_line = text_file.read()
if text_line == "":
    path = raw_input("Enter path for storing downloaded videos: ") # Writes the path for storing downloaded files during first run
    text_file.write(path)
else:
    path = text_line # Takes the path for storing videos from filePath.txt
text_file.close() # Closes the file "filePath.txt"
line = raw_input("Enter complete url of playlist to be downloaded: ")
playlist = line.split('=')[1] # Extracting the playlist id from url
chk = 1
flag = 'check'

def download():
    videoID = link.split('=')[1] # Extracting the video id from url
    url = "http://www.youtube.com/watch?v=" + videoID   
    try:
        yt = YouTube(url)
        video = pafy.new(url)
        name = video.title # Getting name of video
    
        yt.set_filename(name) # Setting name of video
        video = yt.get('mp4', '360p') # This will download an mp4 format video of 360p resolution
    
        print("\nDownloading " + name + "...(Might take several minutes)")
        video.download(path) # Downloading in the specified path
        print("Download completed")
    except:
        print("Video could not be downloaded")

try:
    connection = urllib.urlopen('http://www.youtube.com/playlist?list=' + playlist) # Creating aa connection object to the YouTube playlist
    dom = lxml.html.fromstring(connection.read()) # Reading the page in html format

    for link in dom.xpath('//a/@href'): # checking for hyperlinks in the webpage
        if 'watch?v=' in link and flag != link: # This will ensure only videos are downloaded. Also prevents duplication of videos
            if chk > 2: # This is to prevent duplication of the first video. Without this, it will be downloaded thrice
                download()
                flag = link
            else:
                chk += 1
        else:
            flag = 'check'
except:
    print("\nCould not connect to the URL. Try again later")
