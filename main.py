from pytube import YouTube

# Set the URL of the video you want to download
url = "https://www.youtube.com/watch?v=Eg4niYQCCVc"

# Create a YouTube object
yt = YouTube(url)

# Get the first video in the list of videos
video = yt.streams.filter(mime_type='video/mp4', res='1080p').first()


# Set the filename
if video is not None:
    video.download('C:/Users/Narnacle/Downloads')
else:
    print("No video found with the specified criteria")
