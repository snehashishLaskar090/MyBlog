from flask import *
import json
from data import read_db, write_db

app = Flask(__name__)

Dict = read_db()


@app.route('/', methods = ['GET', 'POST'])
def index():
    Dict = read_db()
    titles = []
    for i in Dict:
        titles.append(i['title'])
    return render_template('index.html', data = Dict,titles = titles)

if __name__ == '__main__':
    app.run(debug=True, host = "127.0.0.1", port= 8000)


