from flask import render_template
from app import *
from app.pdfParserToXML import parsePDFtoXML
import uuid
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
           
from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            from _ast import Str
            filename = str(uuid.uuid1())[:6]+'.pdf'
            
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            resultText = parsePDFtoXML(filepath)
    return resultText
@app.route('/analysis/<filename>')
def analysis(filename):
    return render_template("analysis.html",result='not done yet',)

