# importing the module 
from pytube import YouTube 
import time

# where to save 
# SAVE_PATH = ""

myFile = open('links.txt', 'r')
linkList = myFile.read().split('\n')
myFile.close()

#set base_episode_number to the episode number from which the videos have to be numbered
base_episode_number = 1
episode_number = base_episode_number
pass_count = 0
total_count = 0

for link in linkList :
	# link of the video to be downloaded 
	video_link = link
	total_count += 1

	try: 
		# object creation using YouTube 
		# which was imported in the beginning 
		print('Video No. ' + str(total_count))
		yt = YouTube(video_link, use_oauth=True) 
		print("Title: " + yt.title)

		# filters out the file with "mp4" extension and best resolution
		myVideoStream = yt.streams.filter(progressive = True).order_by('resolution').desc().first()
		print(myVideoStream)

		try: 
			# downloading the video 
			myVideoStream.download(filename = 'myVideo_'+str(episode_number)+'.mp4') 
			pass_count += 1
			print('Video downloaded successfully!')
		except: 
			print("Error in downloading!")
	except: 
		print("Connection Error / Incorrect Link!") #to handle exception 
  
	episode_number += 1
	time.sleep(1)

print()
print('Total videos = ' + str(total_count))
print('Successfully downloaded videos = ' + str(pass_count))
if total_count > 0 :
	print(str(pass_count/total_count*100) + '% Task Completed!!')