from flask import Flask
from flask import render_template
from flask import request
from flask import escape
import sql # Homebrew not-module to talk to my database.
import os
app = Flask(__name__, instance_path = "/web", root_path = "/web")
auth = ['ourtube-sql', 'postgres', 'docker']
os.system("ls /app")
def CleanDescription(i):
    i["description"] = i["description"].replace("\n", "<br />")
    return i
def GetByID(_id):
    return CleanDescription(sql.MatchID(_id)[0])
def GetByTitle(_title):
    newReturn = []
    for i in sql.MatchTitle(_title, auth):
        newReturn.append(CleanDescription(i))
    return newReturn
def GetByLikeTitle(_title):
    newReturn = []
    for i in sql.LikeTitle(f'%{_title}%'m auth):
        CleanDescription(i)
        newReturn.append(i)
    return newReturn
def GetFirst(_num):
    newReturn = []
    for i in sql.GetFirst(_num, auth):
        CleanDescription(i)
        newReturn.append(i)
    return newReturn
@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('home.html')
@app.route('/latest', methods = ['GET', 'POST'])
def latest():
    if request.method == 'POST':
        return title(escape(request.form['search']))
    return render_template('latest.html', descs=GetFirst(5))
@app.route('/search')
def search():
    return render_template('search.html', results = GetByLikeTitle(request.args.get('search')))
@app.route('/id/<video_id>')
def video_id(video_id):
    return render_template('video.html', video=GetByID(video_id))
@app.route('/title/<video_title>')
def title(video_title):
    return render_template('video.html', descs=GetByLikeTitle(video_title))
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 80)
