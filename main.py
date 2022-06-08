from youtube_transcript_api import YouTubeTranscriptApi

from log_tools import log
from publics import ExceptionLine, db


def get_transcript(video_id):
    try:
        return YouTubeTranscriptApi.get_transcript(video_id, languages=['fa'])
    except:
        log.error(f'An error occurred! {ExceptionLine()}')
        return None


from pytube import YouTube, Playlist

playlist_link = "https://www.youtube.com/watch?v=W9wAfqBd_T0&list=PLD018AC9B25A23E16"

col_video = db()['video']
video_links = Playlist(playlist_link).video_urls
i = 1
for link in video_links:
    if col_video.find_one({"url": link}) is None:
        video = YouTube(link)
        print(f"{i}/{len(video_links)} {video.title}")
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
