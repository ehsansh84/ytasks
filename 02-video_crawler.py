from pytube import YouTube, Playlist
from publics import db

# playlist_link = "https://www.youtube.com/watch?v=W9wAfqBd_T0&list=PLD018AC9B25A23E16"

col_video = db()['video']
col_playlist = db()['playlist']
pl_counter = 1
result = col_playlist.find()
for playlist in result:
    print(f"playlist: {pl_counter}/{result.count()}")
    pl_counter += 1
    playlist_link = playlist['url']
    video_links = Playlist(playlist_link).video_urls
    i = 1
    for link in video_links:
        if col_video.find_one({"url": link}) is None:
            video = YouTube(link)
            print(f"video: {i}/{len(video_links)} {video.title}")
            i += 1
            col_video.insert_one({
                "url": link,
                "video_id": video.video_id,
                "title": video.title,
                "views": video.views,
                "author": video.author,
                "channel_id": video.channel_id,
                "channel_url": video.channel_url,
                "keywords": video.keywords,
                "length": video.length,
                "publish_date": video.publish_date,
                "thumbnail_url": video.thumbnail_url,
                "description": video.description,
                "vid_info": video.vid_info,
                "initial_data": video.initial_data,
                "sub": []
            })
