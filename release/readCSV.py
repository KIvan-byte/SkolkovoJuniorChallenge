import csv
import os


def readKeyloggerCSV(filename):
    Number_OF_Keystrokes = {}
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        s = 0
        reader = list(reader)
        for row in reader[1:]:
            element = row[0]
            if element not in Number_OF_Keystrokes:
                Number_OF_Keystrokes[element] = 1
            else:
                Number_OF_Keystrokes[element] += 1
    return Number_OF_Keystrokes

def readAudioCSV(filename):
    Number_OF_Keystrokes = {}
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        reader = list(reader)
        for row in reader[1:]:
            Number_OF_Keystrokes[row[1]] = row[0]
    return Number_OF_Keystrokes

def makeAudioCSV():
    if not os.path.isfile('audio.csv'):
        with open('audio.csv', "w", newline='') as out_file:
            writer = csv.DictWriter(out_file, delimiter=',', fieldnames=['volue', 'time'])
            writer.writeheader()

def writeToCSV(fields):
    with open('audio.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)