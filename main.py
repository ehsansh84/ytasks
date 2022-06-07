from youtube_transcript_api import YouTubeTranscriptApi


def get_transcript(video_id):
    return YouTubeTranscriptApi.get_transcript(video_id, languages=['fa'])


print(get_transcript("8RI0JnB_OaE"))

