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



sub = get_transcript(hasnt_persian_sub)
if sub is not None:
    for item in sub:
        print(item)
