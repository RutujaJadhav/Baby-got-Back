from flask import Flask, render_template, jsonify, request
from Adafruit_CCS811 import Adafruit_CCS811
import RPi.GPIO as GPIO
from twilio.rest import Client
import threading
import urllib
import os
import time
import board
import neopixel
import pandas as pd
import numpy as np
import math
import datetime
import json

"""
INTERNAL FUNCTIONS
-------------------------------------------------
"""

textAlerts = False
riskFactor = False

def twilio_alert(msg):
    global textAlerts
    if textAlerts:
        message = client.messages.create(to='+12067909956',from_='+12062080987',body=msg)

def alert_on():
    pixels.fill((255,0,0))
    pixels.show()

def alert_all(msg):
    twilio_alert(msg)
    alert_on()

def alert_off():
    pixels.fill((0,0,0))
    pixels.show()

def init_CCS811():
    ccs =  Adafruit_CCS811()
    temp = ccs.calculateTemperature()
    ccs.tempOffset = temp - 23.0
    return ccs

def init_NeoPixels():
    pixel_pin = board.D18
    num_pixels = 1
    ORDER = neopixel.GRB
    pixels = neopixel.NeoPixel(pixel_pin,
                               num_pixels,
                               brightness=0.2,
                               auto_write=False,
                               pixel_order=ORDER)
    return pixels

def init_StatusLED():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23,GPIO.OUT)

def init_twilio():
    account_sid = "AC0d464a30a7c6e7fbacd8dab0441ae589"
    auth_token  = "0753453d03c18573e2c09ba41f925a8f"
    client = Client(account_sid, auth_token)
    return client

def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err:
        return False

def lan_job():
    threading.Timer(10.0, lan_job).start()
    if internet_on:
        GPIO.output(23,GPIO.HIGH)
    else:
        GPIO.output(23,GPIO.LOW)

def ccs811_measure():
    threading.Timer(1.0, ccs811_measure).start()
    while not ccs.available():
    	pass
    temp = ccs.calculateTemperature()
    if not ccs.readData():
        tt = time.time()
        co2 = ccs.geteCO2()
        tvoc = ccs.getTVOC()
        temp = temp
        data = [tt,co2,temp,tvoc]
        df.loc[len(df)] = data

def getRiskFactors():
    global riskFactor
    global textAlerts
    threading.Timer(1.0, getRiskFactors).start()
    with open('static/data.json') as json_data:
        d = json.load(json_data)
        highrisk = len(d['highrisk'])>0
        if highrisk:
            if not riskFactor:
                if textAlerts:
                    alert_all("High risk factors in the crib: "+','.join(d['highrisk']))
                else:
                    alert_on()
            else:
                alert_on()
        else:
            alert_off()
        riskFactor = highrisk


"""
ENDPOINTS
----------------------------------------------------------
"""
app = Flask(__name__)

ccs = init_CCS811()
pixels = init_NeoPixels()
client = init_twilio()
risk_factors = getRiskFactors()

df = pd.DataFrame(columns=['time','co2','temp','tvoc'])

alert_off()
init_StatusLED()
lan_job()
ccs811_measure()
getRiskFactors()

@app.route('/')
def index():
    return render_template('dashboard.html')


@app.route('/text_alerts', methods=['GET', 'POST'])
def text_alerts():
    global textAlerts
    global riskFactor
    if request.method == 'POST':
        textAlerts = request.values.get('alerts') == 'true'
        if riskFactor and textAlerts:
            twilio_alert("There are risk factors in the crib")
        resp = jsonify(success=True)
        return resp
    else:
        return jsonify(alerts = textAlerts)

@app.route('/reading')
def reading():
    return render_template('updatedchart.html')

@app.route('/air_quality')
def air_quality():
    if len(df)>0:
        return jsonify(df.iloc[-1].to_dict())
    return jsonify()

@app.route('/air_quality_history')
def air_quality_history():
    lookback = request.args.get('lookback',default = 3600,type=int)
    lookback = time.time()-lookback

    in_range = df[df['time']>lookback]
    num_results = len(in_range)
    if num_results>0:
        data = in_range.sort_values(by='time')
        temp_data = data['temp'].tolist()
        temp_data = [round(x,2) for x in temp_data]
        tvoc_data = data['tvoc'].tolist()
        time_data = data['time'].tolist()
        time_data = [datetime.datetime.fromtimestamp(x).strftime("%X") for x in time_data]
        return jsonify(temp=temp_data,tvoc=tvoc_data,labels=time_data)
    else:
        return jsonify()


if __name__ == '__main__':
    app.run(host='10.19.212.93', debug=True)
