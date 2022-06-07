from youtube_transcript_api import YouTubeTranscriptApi
from log_tools import log
from publics import ExceptionLine

has_persian_sub = "Cd-artSbpXc"
hasnt_persian_sub = "W9wAfqBd_T0"


def get_transcript(video_id):
    try:
        return YouTubeTranscriptApi.get_transcript(video_id, languages=['fa'])
    except:
        log.error(f'An error occurred! {ExceptionLine()}')
        return None


# sub = get_transcript(has_persian_sub)
# if sub is not None:
#     for item in sub:
#         print(item)

from time import time
from pytube import YouTube, Playlist

playlist_link = "https://www.youtube.com/watch?v=W9wAfqBd_T0&list=PLD018AC9B25A23E16"

video_links = Playlist(playlist_link).video_urls
print(video_links)
video_titles = []
start = time()
for link in video_links:
    sub = get_transcript(link.split("=")[1])
    print(link)
    print(sub is None)
    # print(link)
    # print(YouTube(link).title)
    # video_titles.append(YouTube(link).title)

print(f'Time taken: {time() - start}')
