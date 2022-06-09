import os

from publics import db

TRANSCRIPT_DIR = 'transcripts'
if not os.path.exists(TRANSCRIPT_DIR):
    os.mkdir(TRANSCRIPT_DIR)

col_video = db()['video']
print(col_video.count({'subtitle': {'$exists': True, '$ne': None}}))
i = 1
result = col_video.find({'subtitle': {'$exists': True, '$ne': None}}, {'video_id': 1, 'title': 1, 'url': 1, 'subtitle': 1})
for item in result:
    print(f"{i}/{result.count()}")
    i += 1
    f = open(f'{TRANSCRIPT_DIR}/{item["title"]}', 'w')
    ft = open(f'{TRANSCRIPT_DIR}/{item["title"]}-timed', 'w')
    for sub in item['subtitle']:
        f.write(sub['text']+'\n')
        time = int(sub['start'])
        time_str = f"00:{time}" if time < 60 else f"{int(time/60)}:{time % 60}"
        ft.write(f'{time} {sub["text"]}\n')
    f.close()
    ft.close()
    # print(col_video.update_one({'_id': item['_id']}, {'$set': {'subtitle': sub}}))
