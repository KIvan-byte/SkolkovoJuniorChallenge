import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
from readCSV import makeAudioCSV, writeToCSV, readAudioCSV
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from pylab import rcParams
from threading import Thread
from time import sleep


duration = 300
#in seconds


def audio_callback(indata, frames, time, status):
    now = datetime.datetime.now()
    volume_norm = np.linalg.norm(indata) * 10
    writeToCSV([str(volume_norm), str(now.isoformat())])


def startAudioRecording():
    makeAudioCSV()
    while True:
        stream = sd.InputStream(callback=audio_callback)
        with stream:
            sd.sleep(duration * 1000)
        if input('enter ') == 'q':
            break
def show():
    rcParams['figure.figsize'] = 16, 5 # редактирование размера изображения в дюймах, нужно как-то автоматом делать
    Number_OF_Keystrokes = readAudioCSV('audio.csv')
    time = [i for i in range(len(list(Number_OF_Keystrokes)))]
    num = [float(Number_OF_Keystrokes[el]) for el in Number_OF_Keystrokes]
    # for t,n in zip(time,num):
    #     print(t,n)
    # print(num)
    Number_OF_Keystrokes = pd.Series(Number_OF_Keystrokes)

    plt.title("Количество нажатий клавиш")
    plt.plot(time, num, color='r')
    plt_output = plt.gcf()
    plt.show()

# startAudioRecording()
