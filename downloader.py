from __future__ import unicode_literals
import youtube_dl
import csv

# options for youtube_dl f means the quality here we specified as the best available
# Other available values for this parameter
#    best: Select the best quality format represented by a single file with video and audio.
#    worst: Select the worst quality format represented by a single file with video and audio.
#    bestvideo: Select the best quality video-only format (e.g. DASH video). May not be available.
#    worstvideo: Select the worst quality video-only format. May not be available.
#    bestaudio: Select the best quality audio only-format. May not be available.
#    worstaudio: Select the worst quality audio only-format. May not be available.
# Refer here for other options and values https://github.com/ytdl-org/youtube-dl/blob/master/README.md

ydl_opts = {
            'f': 'best'
        }

with open('url_list.csv') as csv_file: #Opening the CSV file with url list
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader: # Loopjing through the url's
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([row[0]]) #asking youtube_dl to dowload the current url from csv list