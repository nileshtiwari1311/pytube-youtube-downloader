# importing the module 
from pytube import YouTube

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

	# filters out the file with "mp4" extension and best resolution
	myVideoStream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
	print(myVideoStream)
	print()

	try: 
		# downloading the video 
		myVideoStream.download(filename='myVideo.mp4')
		# use this to save the file to a specific directory
		# myVideoStream.download(output_path=SAVE_PATH, filename='myVideo')
		print('Video downloaded successfully!')
	except: 
		print("Error in downloading!")
except: 
	print("Connection Error / Incorrect Link!") #to handle exception