from __future__ import unicode_literals
import youtube_dl
import csv

ydl_opts = {
            'f': 'best'
        }

with open('url_list.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([row[0]])