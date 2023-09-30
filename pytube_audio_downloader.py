# importing the module 
from pytube import YouTube
import os

# where to save 
# SAVE_PATH = ""

# link of the video to be downloaded 
video_link = "https://www.youtube.com/watch?v=5piylWK7fWA"

try: 
	# object creation using YouTube 
	# which was imported in the beginning
	yt = YouTube(video_link, use_oauth=True) 
	print("Title: " + yt.title)
	print()

	# filters out the audio with best quality
	myAudioStream = yt.streams.filter(only_audio=True).first()
	print(myAudioStream)
	print()

	try:
		# downloading the audio in a .mp4 file
		myAudioStream.download(filename='myAudio.mp4')
		os.system('ffmpeg -hide_banner -i myAudio.mp4 myAudio.mp3')
		os.system('rm -f myAudio.mp4')
		# use this to save the file to a specific directory
		# myAudioStream.download(output_path=SAVE_PATH, filename='myAudio')
		print('Audio downloaded successfully!')
	except: 
		print("Error in downloading!")
except: 
	print("Connection Error / Incorrect Link!") #to handle exception