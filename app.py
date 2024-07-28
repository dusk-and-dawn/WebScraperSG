from flask import Flask, render_template, send_file
import gridfs
from io import BytesIO
from db import get_client
app = Flask(__name__)
db = get_client()
fs= gridfs.GridFS(db)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/image/<filename>')
# def get_image(filename):
#     image_data = fs.get_last_version(filename=filename).read()
#     return send_file(BytesIO(image_data), mimetype='image/jpeg')
    
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
    return render_template('WTAcountries.html')

if __name__ == '__main__':
    app.run(debug=True)