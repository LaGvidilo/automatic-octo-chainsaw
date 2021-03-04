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
from PIL import Image, ImageDraw, ImageFont
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
import urllib3
#==============================
def create_app():
    app = Flask(__name__,template_folder="templates",static_folder="static")
    app.secret_key = os.urandom(4096)
    app.WTF_CSRF_SECRET_KEY = os.urandom(4096)
    #CORS(app)
    csrf = CSRFProtect()
    csrf.init_app(app)
    #==================================================
    @app.route('/get_badge_meteo/H/IN',methods=["GET"])
    def getter_badge_humidity_in():
        http = urllib3.PoolManager()
        url = http.request('GET', 'https://meteo.local.rick.informabox.tech/call/DHT11-SENSORS/o1/1')
        code = url.data
        json_data = json.loads(code)
        with Image.open("assets/button1_pushed.png") as im:
            imd = ImageDraw.Draw(im)
            fontsize = 11
            font = ImageFont.truetype("arial.ttf", fontsize)
            imd.text((im.size[0]/4,im.size[1]/2.8),"{}%".format(str(json_data["humidity_IN"])),fill=(0,0,0),font=font)
            im.save("static/img0_meteo.png")
        return app.send_static_file("img0_meteo.png")
    #==============================
    @app.route('/get_badge_meteo/H/OUT',methods=["GET"])
    def getter_badge_humidity_out():
        http = urllib3.PoolManager()
        url = http.request('GET', 'https://meteo.local.rick.informabox.tech/call/DHT11-SENSORS/o1/1')
        code = url.data
        json_data = json.loads(code)
        with Image.open("assets/button1_pushed.png") as im:
            imd = ImageDraw.Draw(im)
            fontsize = 11
            font = ImageFont.truetype("arial.ttf", fontsize)
            imd.text((im.size[0]/4,im.size[1]/2.8),"{}%".format(str(json_data["humidity_OUT"])),fill=(0,0,0),font=font)
            im.save("static/img1_meteo.png")
        return app.send_static_file("img1_meteo.png")
    #==============================
    @app.route('/get_badge_meteo/T/IN',methods=["GET"])
    def getter_badge_temperature_in():
        http = urllib3.PoolManager()
        url = http.request('GET', 'https://meteo.local.rick.informabox.tech/call/DHT11-SENSORS/o1/1')
        code = url.data
        json_data = json.loads(code)
        with Image.open("assets/button1_pushed.png") as im:
            imd = ImageDraw.Draw(im)
            fontsize = 11
            font = ImageFont.truetype("arial.ttf", fontsize)
            imd.text((im.size[0]/4,im.size[1]/2.8),"{}°C".format(str(json_data["temperature_IN"])),fill=(0,0,0),font=font)
            im.save("static/img2_meteo.png")
        return app.send_static_file("img2_meteo.png")
    #==============================
    @app.route('/get_badge_meteo/T/OUT',methods=["GET"])
    def getter_badge_temperature_out():
        http = urllib3.PoolManager()
        url = http.request('GET', 'https://meteo.local.rick.informabox.tech/call/DHT11-SENSORS/o1/1')
        code = url.data
        json_data = json.loads(code)
        with Image.open("assets/button1_pushed.png") as im:
            imd = ImageDraw.Draw(im)
            fontsize = 11
            font = ImageFont.truetype("arial.ttf", fontsize)
            imd.text((im.size[0]/4,im.size[1]/2.8),"{}°C".format(str(json_data["temperature_OUT"])),fill=(0,0,0),font=font)
            im.save("static/img3_meteo.png")
        return app.send_static_file("img3_meteo.png")
    #==============================

    #==================================================
    #for just use... you know... that:
    #app.run("127.0.0.1",8005,True)
    #or launch command: gunicorn3 -b '127.0.0.1':'8005' --workers=4 'aocAPI:create_app()'
    return app
#============================================================