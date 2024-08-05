from flask import Flask, render_template, send_file, url_for
import gridfs
from io import BytesIO
from db import get_client, get_from_db
from datetime import datetime

app = Flask(__name__)
db = get_client()
fs= gridfs.GridFS(db)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/graph/<key>')
def return_graph(key):
    document = db.tennis.find_one({'name': key})
    if document is None:
        return 'No document found', 404
    image_binary = document['img']
    buffer = BytesIO(image_binary)
    buffer.seek(0)
    return send_file(buffer, mimetype='image/png')

@app.route('/WTAcountries', methods=('POST', 'GET'))
def WTAcountries():
    top100 = get_from_db('countries100_ranked')
    top5 = top100['content'][:5]
    top500 = get_from_db('countries_ranked')
    print(top500)
    top5_500 = top500['content'][:5]
    print(top5_500)
    return render_template('WTAcountries.html', top5=top5, top5_500=top5_500)

if __name__ == '__main__':
    app.run(debug=True)