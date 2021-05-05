
from readCSV import writeaudio
import numpy as np
import datetime
import pyaudio

audio = True

def stop_audio():
    global audio
    audio = False


def startAudioRecording():
    global audio
    CHUNK = 2 ** 11
    RATE = 44100
    print("start audio recording")
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)
    while audio:  # go for a few seconds
        data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
        peak = np.average(np.abs(data)) * 2
        now = datetime.datetime.now()
        writeaudio([str(peak), str(now.isoformat())])

    stream.stop_stream()
    stream.close()
    p.terminate()
    print("stop audio recording")