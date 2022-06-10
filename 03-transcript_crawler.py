from youtube_transcript_api import YouTubeTranscriptApi
from log_tools import log
from publics import ExceptionLine, db


def get_transcript(video_id):
    try:
        return YouTubeTranscriptApi.get_transcript(video_id, languages=['fa'])
    except:
        log.error(f'An error occurred! {ExceptionLine()}')
        return None
re
col_video = db()['video']
for item in col_video.find({'subtitle': {'$exists': False}}, {'video_id': 1}):
    sub = get_transcript(item['video_id'])
    print(col_video.update_one({'_id': item['_id']}, {'$set': {'subtitle': sub}}))
