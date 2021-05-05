try:
    import sys
    from sys import exit
except:
    print('sys')
# sys.exit()
from recording import stop_recording, start_recording

try:
    from PySide6 import QtCore, QtWidgets, QtGui
except:
    print('PySide6')

from keylogger import start_keylogger, stop_keylogger

try:
    import threading
except:
    print('threading')

try:
    import csv
except:
    print('csv')

try:
    import os
except:
    print('os')
from readCSV import makeAudioCSV, makeKeylogerCSV, makeMouseCSV, readAudioCSV, readKeyloggerCSV, readTimeKeys
from audio import stop_audio, startAudioRecording
try:
    from multiprocessing import Process
except:
    print('multiprocessing')

from Mouse import lst
import time
#
# except:
#     print('Установите необходимые библиотеки')
#     sys.exit()


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        if not os.path.isdir('Videos'):
            os.mkdir('Videos')
        if not os.path.isdir('CSV_files'):
            os.mkdir('CSV_files')
        self.count = 1
        super().__init__()
        self.statistic_string = f"Самая часто нажимаемая клавиша: {0}\n\nКоличество пиковых моментов игры: {0}\n\nЧастота нажатия клавиш: {0}\n\n"
        self.traker = False
        self.processes = []
        self.button = QtWidgets.QPushButton("Start")
        self.button2 = QtWidgets.QPushButton("Stop")
        self.text = QtWidgets.QLabel(self.statistic_string)
        self.setWindowTitle('ProScience')
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)

        self.button.clicked.connect(self.magic)
        self.button2.clicked.connect(self.stop)

    @QtCore.Slot()
    def magic(self):
        if not self.traker:
            self.makeCSV()
            self.keylogger = Process(target=start_keylogger, daemon=True)
            self.processes.append(self.keylogger)
            self.recording = Process(target=start_recording, args=(self.count,), daemon=True)
            self.processes.append(self.recording)
            self.audio = Process(target=startAudioRecording, daemon=True)
            self.processes.append(self.audio)
            self.mouse = Process(target=lst, daemon=True)
            self.processes.append(self.mouse)
            self.keylogger.start()
            self.recording.start()
            self.audio.start()
            self.mouse.start()
            print('processes start')
            self.traker = True
            time.sleep(2)
            self.text.setText(f"Самая часто нажимаемая клавиша: {0}\n\nКоличество пиковых моментов игры: {0}\n\nЧастота нажатия клавиш: {0}\n\nПрограмма запущена. Для остановки нажмите 'Стоп' ")
            self.count += 1

    @QtCore.Slot()
    def stop(self):
        self.traker = False
        stop_recording()
        stop_keylogger()
        stop_audio()
        time.sleep(0.5)
        for proc in self.processes:
            proc.terminate()
        print("processes terminate")
        self.statistics()



    def closeEvent(self, event):
        stop_recording()
        stop_keylogger()
        stop_audio()
        time.sleep(0.5)
        for proc in self.processes:
            proc.terminate()

    def makeCSV(self):
        makeKeylogerCSV()
        makeAudioCSV()
        makeMouseCSV()

    def statistics(self):
        try:
            maxKey = readKeyloggerCSV('CSV_files/keys.csv')
            max = 0
            if maxKey:
                max = sorted(maxKey.items(), key=lambda x: x[1], reverse=True)[0][0]
            audioStat = readAudioCSV('CSV_files/audio.csv')
            audiost = 0
            for time in audioStat:
                if float(audioStat[time]) >= 15000:
                    audiost += 1
            self.text.setText(f"Самая часто нажимаемая клавиша: {max}\n\nКоличество пиковых моментов игры: {audiost}\n\nЧастота нажатия клавиш: {readTimeKeys()}\n\nЗапись завершена")
            print('sucsess')
        except Exception as e:
            pass




def main():
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(300, 200)
    widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    process_one = Process(target=main)
    process_one.start()
    process_one.join()
