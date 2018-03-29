#!/usr/bin/env python3
from flask import Flask, json, request
import csv
from datetime import datetime
import os.path

from .settings import config

app = Flask(__name__)
app.config.from_object(config)
app.config.from_envvar('PLANTSERVER_SETTINGS', silent=True)


@app.route('/')
def home():
    return ('<a href="https://github.com/wardweistra/plantserver">PlantServer</a>')

@app.route('/log', methods=['POST'])
def log():
    now = datetime.now()
    date_string = now.date().strftime("%Y_%m_%d")
    time_string = now.time().strftime("%H:%M:%S")
    requestdata = json.loads(request.get_data())
    version = requestdata['version']
    data = requestdata['data']
    
    logfile = 'sensorlog.tsv'
    filenew = False
    if os.path.isfile(logfile):
        logcsv = open(logfile, 'a')
    else:
        logcsv = open(logfile, 'w')
        filenew = True
    logfieldnames = ["date","time","sensor","value", "version"]
    logcsvwriter = csv.DictWriter(
        logcsv, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL,
        fieldnames=logfieldnames)
    if filenew:
        logcsvwriter.writeheader()
    
    for sensor in data:
        logcsvwriter.writerow({
            'date': date_string,
            'time': time_string,
            'sensor': sensor,
            'value': data[sensor],
            'version': version
        })
    
    logcsv.close()
    
    return ('', 200)

if __name__ == '__main__':
    app.run()
