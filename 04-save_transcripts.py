import os

from publics import db, ExceptionLine

TRANSCRIPT_DIR = 'transcripts-teded'
if not os.path.exists(TRANSCRIPT_DIR):
    os.mkdir(TRANSCRIPT_DIR)

col_video = db()['video']
# print(col_video.count({'subtitle': {'$exists': True, '$ne': None}}))
i = 1
result = col_video.find({'subtitle': {'$exists': True, '$ne': None}, 'download': {'$exists': False}}, {'video_id': 1, 'title': 1, 'url': 1, 'subtitle': 1}).limit(100)
# result = col_video.find({'title': {'$regex': '.*extinction.*'}})
# print(result.count())
# print(len(result))
for item in result:
    # print(item)
    # break
    # print(f"{i}/{result.count()}")
    try:
        i += 1
        f = open(f'{TRANSCRIPT_DIR}/{item["title"]}', 'w')
        ft = open(f'{TRANSCRIPT_DIR}/{item["title"]}-timed', 'w')
        print(item['title'])
        for sub in item['subtitle']:
            f.write(sub['text'] + '\n')
            time = int(sub['start'])
            time_str = f"00:{time}" if time < 60 else f"{int(time / 60)}:{time % 60}"
            # print(time_str)
            ft.write(f'{time_str} {sub["text"]}\n')
        f.close()
        ft.close()
        col_video.update_one({'_id': item['_id']}, {'$set': {'download': True}})
    except:
        print(ExceptionLine())
    # print(col_video.update_one({'_id': item['_id']}, {'$set': {'subtitle': sub}}))
