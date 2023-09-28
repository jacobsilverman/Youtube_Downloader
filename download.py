import yt_dlp as youtube_dl
import os

# Define the path to the cookies file, download the cookie file using the GET cookies.txt LOCALLY
cookies_path = 'C:/Users/username/Desktop/yt_cookies.txt' # change this path based on where you save your file
url = 'https://www.youtube.com/urlofyourvideo'

# Check if the cookies file exists
if os.path.exists(cookies_path):
    print("Cookies file found at:", cookies_path)

    # Set the options for yt-dlp
    ydl_opts = {
      'outtmpl': './videos/%(title)s.%(ext)s',  # Save the file with the video's title and extension in the video folder
      'format': 'bestvideo[ext=mp4][vcodec=h264]+bestaudio[ext=m4a][acodec=aac]/best[ext=mp4]/best',
      'cookiesfile': cookies_path,  # Specify the cookies file
      'source_address': '0.0.0.0',  # Specify the source address to bypass geo-restrictions
      'retries': 2  # Retry up to 5 times in case of issues
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            print("Error:", str(e))
            print("Trying to download a lower quality format...")
            ydl_opts['format'] = 'best[ext=mp4]'
            ydl.download([url])
else:
    print("Cookies file not found at:", cookies_path)