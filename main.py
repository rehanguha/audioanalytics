#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:58:29 2020

@author: rehanguha
"""
from src.utils import extractFilename, mkDIR
from flask import Flask, request, json, send_file
# import speech_recognition as sr
from os import path
import os
from wit import Wit
import src.audioanalysis as aa
import src.wavefile as wave
from IPython import embed
from flask_cors import CORS
from src.CONSTANTS import *
from src.pyaa import zcr_sigenergy, feature_extraction
import glob

app = Flask(__name__)
cors = CORS(app)

client = Wit(WIT_AI_KEY)

# /listAudioFiles?foldername=<folder>
@app.route("/listAudioFiles", methods = ['GET', 'POST'])
def listAudioFiles():
    folder = request.args.get('foldername')
    filelist = glob.glob(folder+'/*.wav')
    return json.jsonify(filelist)

# /transcribe?filename= <inputfilename with path>
@app.route("/transcribe", methods = ['GET', 'POST'])
def transcribe():
    AUDIO_FILE = request.args.get('filename')
    
    with open(AUDIO_FILE, 'rb') as f:
        resp = client.speech(f, None, {'Content-Type': 'audio/wav'})
    text = resp["_text"]
    word_frequency = {}
    for word in text.split():
        if word in word_frequency.keys():
            word_frequency[word] = word_frequency[word] + 1
        else:
            word_frequency[word] = 1
    resp.update({'word_frequency': word_frequency})
    name = extractFilename(AUDIO_FILE)
    outputpath = "output/" + str(name) + "/"
    with open(outputpath + 'transcribe.json', 'w') as transcribe: 
        transcribe.write(json.dumps(resp))     
    return(json.jsonify(resp))       


# /quantileanalysis?filename=<inputfilename>
@app.route("/quantileanalysis", methods = ['GET', 'POST'])
def quantileanalysis():
    filename = request.args.get('filename')
    data = aa.mysptotal(filename, PRAAT_FILE)
    return json.dumps(data)

@app.route("/transcribe_data", methods = ['GET'])
def transcribe_data():
    filename = request.args.get('filename')
    name = extractFilename(filename)
    data = {}
    path = "output/" + str(name) + "/"
    with open(path + 'transcribe.json', 'r') as transcribe: 
        data = transcribe.read()
    return data


# /waveform?filename=<inputfilename with path>
@app.route("/waveform", methods = ['GET', 'POST'])
def waveform():
    filename = request.args.get('filename')
    name = extractFilename(filename)
    outputpath = "output/" + str(name) + "/"
    mkDIR(outputpath)
    status = wave.audio_waveplot(INPUTPATH=filename,OUTPATH=outputpath)
    return status

@app.route("/spec_image", methods = ['GET'])
def spec_image():
    filename = request.args.get('filename')
    name = extractFilename(filename)
    return send_file('output/' + name + '/spec.png', attachment_filename='spec.png', mimetype='image/png')

@app.route("/wave_image", methods = ['GET'])
def wave_image():
    filename = request.args.get('filename')
    name = extractFilename(filename)
    return send_file('output/' + name + '/waveplot.png', attachment_filename='waveplot.png', mimetype='image/png')

@app.route("/analyze_image", methods = ['GET'])
def analyze_image():
    filename = request.args.get('filename')
    name = extractFilename(filename)
    return send_file('output/' + name + '/zcr_energy.png', attachment_filename='zcr_energy.png', mimetype='image/png')    

# /analyze?filename=<inputfilename with path>
@app.route("/analyze", methods = ['GET', 'POST'])
def analyze():
    filename = request.args.get('filename')
    name = extractFilename(filename)
    outputpath = "output/" + str(name) + "/"
    mkDIR(outputpath)
    status = zcr_sigenergy(INPUTPATH=filename, OUTPATH=outputpath)
    return status
    

# /fe?filename=<inputfilename with path>
@app.route("/fe", methods = ['GET', 'POST'])
def fe():
    filename = request.args.get('filename')
    name = extractFilename(filename)
    outputpath = "output/" + str(name) + "/"
    mkDIR(outputpath)

    status = feature_extraction(INPUTPATH=filename, OUTPATH=outputpath)
    
    return status


if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=5001)