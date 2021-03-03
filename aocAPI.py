#!/usr/bin/pytho0n3
#coding: utf-8
#============================================================
from flask import Flask, escape, request
from flask import flash, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from copy import deepcopy
import os, hashlib, gzip
from base64 import b64encode as b64enc
from base64 import b64decode as b64dec
#from flask_cors import CORS
import requests
import json
from datetime import datetime
from flask_wtf.csrf import CSRFProtect
from PIL import Image
# =====================================
from multiprocessing import Process
# =====================================
def filter_value_conv(value,ifis=[None],totype=str):
    if value in ifis:
        return totype(value)
    return value
#==============================
def filter_no_smoke(strarg):
    out = ""
    if type(strarg) == str:
        for i in strarg:
            if i in ".0123456789":
                out = out + i 
    return out
#==================================================
#==============================
import time
from datetime import datetime
#==============================
def create_app():
    app = Flask(__name__,template_folder="templates",static_folder="static")
    app.secret_key = os.urandom(4096)
    app.WTF_CSRF_SECRET_KEY = os.urandom(4096)
    #CORS(app)
    csrf = CSRFProtect()
    csrf.init_app(app)
    #==================================================
    @app.route('/get_badge_meteo_outdoor',methods=["GET"])
    def about_the_node_func():
        with Image.open("button1_normal.png") as im:
            im.text((im.size[0]/2,im.size[1]/2,"Hello",align="center"))
            im.save("/static/img1_meteo.png")
        return templates("test_construct_1.tpl")
    #==================================================
    #for just use... you know... that:
    #app.run("127.0.0.1",8000,True)
    #or launch command: gunicorn3 -b '127.0.0.1':'8000' --workers=2 'nodeAPI:create_app()'
    return app
#============================================================