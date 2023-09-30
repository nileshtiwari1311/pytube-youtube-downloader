# importing the module 
from pytube import YouTube 
import time

# where to save 
# SAVE_PATH = "/home/nilesh/Videos/tmkoc"

myFile = open('url_list.txt', 'r')
linkList = myFile.read().split('\n')
myFile.close()

#set base_episode_number to the episode number/index in the list from which the videos have to be downloaded 
base_episode_number = 2
no_of_episodes = 2
episode_number = base_episode_number
pass_count = 0
index = 0

for link in linkList :
	# link of the video to be downloaded 
	video_link = link
	index += 1

	if index < base_episode_number :
		continue

	try: 
		# object creation using YouTube 
		# which was imported in the beginning 
		print('Video No. ' + str(index))
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

	if episode_number == base_episode_number+no_of_episodes :
		break
	time.sleep(1)

print()
print('Total videos = ' + str(no_of_episodes))
print('Successfully downloaded videos = ' + str(pass_count))
if no_of_episodes > 0 :
	print(str(pass_count/no_of_episodes*100) + '% Task Completed!!')