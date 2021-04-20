import sys
import recording
from PySide6 import QtCore, QtWidgets, QtGui
from keylogger import start_keylogger, stop
import threading
import csv
import os


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.traker = False
        self.makeCSV()
        self.button = QtWidgets.QPushButton("Start")
        self.button2 = QtWidgets.QPushButton("Stop")
        self.text = QtWidgets.QLabel("Hello World")
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
            print('button')
            th = threading.Thread(target=start_keylogger, daemon=True)
            th.start()


    @QtCore.Slot()
    def stop(self):
        stop()



    def closeEvent(self, event):
        stop()


    def makeCSV(self):
        if not os.path.isfile('keys.csv'):
            with open('keys.csv', "w", newline='') as out_file:
                writer = csv.DictWriter(out_file, delimiter=',', fieldnames=['key', 'time'])
                writer.writeheader()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(300, 200)
    widget.show()
    sys.exit(app.exec_())
