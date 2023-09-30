from pytube import Playlist, YouTube
import time
import os

bad_chars = ['|', '/', '<', '>', ':', '\"', '\\', '?', '*', '%', '.', ',', ';', '=']

p = Playlist("https://www.youtube.com/playlist?list=PLzufeTFnhupxlWdoBeNJg1PSwlcVEW2iz")

#set base_episode_number to the episode number/index from which the videos have to be downloaded 
base_episode_number = 1
no_of_episodes = 2
episode_number = base_episode_number
pass_count = 0
total_count = 0

for url in p.video_urls :
	total_count += 1

	# skip to base episode number/index in the playlist
	if total_count < base_episode_number :
		continue

	try: 
		# object creation using YouTube 
		# which was imported in the beginning 
		video = YouTube(url, use_oauth=True)
		print('Video No. ' + str(total_count))
		print("Title: " + video.title)
		# if using title of the video as filename
		filename = ''.join(i for i in video.title if not i in bad_chars)

		# filters out the file with "mp4" extension and best resolution
		myAudioStream = video.streams.filter(only_audio=True).first()
		print(myAudioStream)

		try: 
			# downloading the video 
			myAudioStream.download(filename = 'myAudio.mp4')
			# os.system('ffmpeg -hide_banner -i myAudio.mp4 \"myAudio_' + str(episode_number) + '.mp3\"')
			# if using title of the video as filename
			os.system('ffmpeg -hide_banner -i myAudio.mp4 \"' + filename + '.mp3\"')
			pass_count += 1
			print('Audio downloaded successfully!')
		except: 
			print("Error in downloading!")
	except: 
		print("Connection Error / Incorrect Link!") #to handle exception 

	episode_number += 1

	# download only those many episodes equal to the value of no_of_episodes 
	if episode_number == (base_episode_number+no_of_episodes) :
		os.system('rm -f myAudio.mp4')
		break

	time.sleep(1)

print()
print('Total audios = ' + str(no_of_episodes))
print('Successfully downloaded audios = ' + str(pass_count))
if no_of_episodes > 0 :
	print(str(pass_count/no_of_episodes*100) + '% Task Completed!!')