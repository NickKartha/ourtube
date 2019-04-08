from flask import Flask
from flask import render_template
from flask import request
from flask import escape
import sql # Homebrew not-module to talk to my database.
import os
app = Flask(__name__, instance_path = "/web", root_path = "/web")
auth = ['ourtube-sql', 'postgres', 'docker']
os.system("ls /app")
def clean_description(i):
    i[4] = i[4].replace("\n", "<br />")
    return i
def get_by_id(_id):
    return clean_description(sql.match_id(_id, auth)[0])
def get_by_title(_title):
    retval = []
    for i in sql.match_title(_title, auth):
        retval.append(clean_description(i))
    return retval
def get_by_like_title(_title):
    retval = []
    print(_title)
    for i in sql.like_title(f'%{_title}%', auth):
        clean_description(i)
        retval.append(i)
    return retval
def get_first(_num):
    retval = []
    for i in sql.get_first(_num, auth):
        clean_description(i)
        retval.append(i)
    return retval
def get_by_playlist_id(_id):
    retval = []
    match_playlist = sql.match_playlist_id(_id, auth)
    for i in match_playlist[0][1]:
        retval.append(get_by_id(i))
    return [retval, match_playlist[0][2]]
@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('home.html')
@app.route('/latest', methods = ['GET', 'POST'])
def latest():
    if request.method == 'POST':
        return title(escape(request.form['search']))
    return render_template('latest.html', descs=get_first(5))
@app.route('/search')
def search():
    return render_template('search.html', results = get_by_like_title(request.args.get('search')))
@app.route('/id/<video_id>')
def video_id(video_id):
    return render_template('video.html', video=get_by_id(video_id))
@app.route('/title/<video_title>')
def title(video_title):
    return render_template('video.html', descs=get_by_like_title(video_title))
@app.route('/playlist/<playlist_id>')
def playlist(playlist_id):
    playlist_data = get_by_playlist_id(playlist_id)
    if request.args.get('id'):
        return render_template('video.html', video = get_by_id(request.args.get('id')), playlist = playlist_data)
    else:
        return render_template('playlist.html', results = playlist_data[0], playlist_name = playlist_data[1])
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 80)
