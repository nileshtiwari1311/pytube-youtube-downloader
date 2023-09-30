from pytube import Playlist

p = Playlist("https://www.youtube.com/playlist?list=PLzufeTFnhupxlWdoBeNJg1PSwlcVEW2iz")
f = open('urls.txt', 'w')

for url in p.video_urls :
	f.write(url)
	f.write('\n')

f.close()