from pytube import YouTube, Playlist
from publics import db

col_playlist = db()['playlist']
f = open('links.txt', 'r')
channel_name = ''
for line in f.readlines():
    if line[0] == '-':
        channel_name = line.split(' ')[1].strip()
        print(channel_name)
    else:
        # print()
        url = line.strip()
        if col_playlist.find_one({'url': url}) is None:
            print(col_playlist.insert_one({
                'channel_name': channel_name,
                'url': url
            }))
