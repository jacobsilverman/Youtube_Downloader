# Youtube_Downloader
simple python script where you can easily download a youtube video as a mp4 based on the url provided in the highest quality available for the video

# Setup:
1. For some videos that are mature will need youtube authetication which is provided when you log into an account over 18. However you need these cookies from that login so the best way to get this is with the chrome extension 'Get cookies.txt LOCALLY' to export your cookies as a txt after logging into youtube and then make sure you know the path for this file which you update in the download.py script

2. pip install yt_dlp this is the best software to use that works really well to maintain the quality of the video you are downloading

3. go into the download.py and change these 3 variables
cookies_path - where you saved your cookies for session login on your youtube account
url - the url you want to download
outtmpl - the output location of the video

That should be all the steps that are neccessary. If any problems occur please feel free to reach out to jacob.h.silverman@gmail.com or post a issue on the repo. Thank you!