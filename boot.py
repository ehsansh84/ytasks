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


app.run(host='0.0.0.0', port=8001)
