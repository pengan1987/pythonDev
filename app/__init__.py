# -*- coding: utf-8 -*-  
import os
from flask import Flask,  redirect, url_for




app = Flask(__name__)
app.config.from_object('app.config')

from app import views
