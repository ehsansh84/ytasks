from flask import Flask
from flask import render_template
from publics import db
app = Flask(__name__)


@app.route('/')
def home():
    return 'Web App with Python Flask!'


@app.route('/index')
def index():
    name = 'Ehsan'
    return render_template('index.html', title='Welcome', username=name)


@app.route('/playlist')
def playlist():
    col_playlist = db()['playlist']
    result = col_playlist.find().limit(10)
    data = []
    for item in result:
        data.append(item)
        print(item)
    # name = 'Ehsan'
    return render_template('playlist.html', title='Playlists', playlists=data)


@app.route('/video')
def video():
    col_video = db()['video']
    result = col_video.find({'subtitle': {'$ne': None}}, {'title': 1, 'views': 1, 'author': 1, 'channel_url': 1, 'url': 1, 'length': 1, 'thumbnail_url': 1}).limit(10)
    data = []
    for item in result:
        data.append(item)
        print(item)
    # name = 'Ehsan'
    return render_template('video.html', title='Videos', data=data)


app.run(host='0.0.0.0', port=8000)
