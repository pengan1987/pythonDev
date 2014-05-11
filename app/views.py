from flask import render_template
from app import *
from app.pdfParsers import parsePDFtoHTML,parsePDFtoText

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
            filename = str(uuid.uuid1())[:6]+'.pdf'
            
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            if (request.form.has_key('toHTML')):
                resultHtml = parsePDFtoHTML(filepath)
                return resultHtml
            else:
                resultText = parsePDFtoText(filepath)
                return render_template("result.html",result=resultText)
    return render_template("index.html",title='Home',)
@app.route('/analysis/<filename>')
def analysis(filename):
    return render_template("analysis.html",result='not done yet',)

