# 光スペアナで取得したデータをもとにスペクトルを平たん化する
# それに使用したwspファイルを保存する。

import requests
import json
import os
from WSMethods import *
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d

osaFileName = '/20210606/initial_spectrum.csv'

# 光スペアナで取得したデータを読み込む
spectrumData = np.loadtxt(osaFileName, delimiter=",", dtype = "unicode")

# Define device IP
ip = '169.254.6.8'
# Get device info 
result = requests.get('http://' + ip + '/waveshaper/devinfo').json()

# Set frequency variables from device info
s = result['startfreq']
e = result['stopfreq']

# Create data for wsp
wsFreq = np.linspace(s, e, (e-s)/0.001 + 1)
wsAttn = 50*np.power(np.sin(2*np.pi/0.5*(wsFreq-193)),2)
wsPhase = np.zeros(wsFreq.shape)
wsPort = np.ones(wsFreq.shape)

# Upload profile using created data
r = uploadProfile(ip, wsFreq, wsAttn, wsPhase, wsPort)