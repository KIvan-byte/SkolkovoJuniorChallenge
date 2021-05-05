import csv
import os
import datetime

def readTimeKeys():
    with open('CSV_files/keys.csv', "r", newline="") as file:
        reader = csv.reader(file)
        reader = list(reader)
        if len(reader) == 1:
            return 0
        t1, t2 = datetime.datetime.strptime(reader[1][1], '%Y-%m-%dT%H:%M:%S.%f'), datetime.datetime.strptime(reader[-1][1], '%Y-%m-%dT%H:%M:%S.%f')
        keyst = (len(reader))/(((t2 - t1).total_seconds())/60)
    return keyst

def readKeyloggerCSV(filename) -> dict:
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


def readAudioCSV(filename) -> dict:
    Number_OF_Keystrokes = {}
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        reader = list(reader)
        for row in reader[1:]:
            Number_OF_Keystrokes[row[1]] = row[0]
    return Number_OF_Keystrokes


def makeAudioCSV():
    if not os.path.isfile('CSV_files/audio.csv'):
        with open('CSV_files/audio.csv', "w", newline='') as out_file:
            writer = csv.DictWriter(out_file, delimiter=',', fieldnames=['volue', 'time'])
            writer.writeheader()


def writeaudio(fields):
    with open('CSV_files/audio.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)


def readMouseGrafCSV(filename) -> dict:
    mt = {}
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        reader = list(reader)
        for row in reader[1:]:
            mt[row[0]] = row[1]
    return mt

def makeKeylogerCSV():
    with open('CSV_files/keys.csv', "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=['key', 'time'])
        writer.writeheader()


def makeMouseCSV():
    with open('CSV_files/mouse.csv', "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=['time','x','y', 'clicked'])
        writer.writeheader()
    with open('CSV_files/mousegraf.csv', "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=['time','transfer'])
        writer.writeheader()


def writeToCSV(fields):
    with open('CSV_files/mouse.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

def writeToMouseGraf(fields):
    with open('CSV_files/mousegraf.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)