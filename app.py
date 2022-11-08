# Author : Snehashish Laskar

from flask import *
from flask_session import Session
import db

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/', methods=['GET'])
def index():
    data = db.readDb()
    return render_template('index.html', data=data)

@app.route('/new', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        if 'login' in request.form:
            password = request.form['password']

            if password == 'snehashish08036#@#':
                return render_template('add-post.html',login = True)
            else:
                return render_template('add-post.html',login = False)
        else:
            title = request.form['title']
            date = request.form['date']
            txt = request.form['txt']
            body = txt.split('\r\n')

            db.addPost(title, date, body)
            return redirect('/')
    else:
        return render_template('add-post.html', login = False)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 8000)