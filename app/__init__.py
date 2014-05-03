import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'D:\pythonDev\uploads'
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
from app import views
