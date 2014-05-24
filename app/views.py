from flask import render_template
from app import app
from flask import request
from os import path,remove
from werkzeug.utils import secure_filename
from app.lib import requestProcessor
import uuid

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
           
from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        fileStream = request.files['file']
        if fileStream and allowed_file(fileStream.filename):
            filename = secure_filename(fileStream.filename)
            filename = str(uuid.uuid1())[:6]+'.pdf'
            # These code is for save file stream to local temp file, then process with local file
            #filepath = path.join(app.config['UPLOAD_FOLDER'], filename)
            #fileStream.save(filepath)
            #result = requestProcessor.parseRequestWithLocalPath(request, fileStream)
            result = requestProcessor.parseRequest(request, fileStream)
            return result
    return render_template("index.html",title='Home',)

@app.route('/analysis/<filename>')
def analysis(filename):
    return render_template("analysis.html",result='not done yet',)

