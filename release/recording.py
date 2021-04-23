import pyautogui
import cv2
import numpy as np
import helper_recording
traker = True

def stop_recording():
    global traker
    traker = False

def start_recording():
    print("start recording thread")
    p=pyautogui.size()
    resolution = (p[0],p[1]//2)
    codec = cv2.VideoWriter_fourcc(*"XVID")
    filename = "__RECORDING__.avi"
    fps = 4.0
    out = cv2.VideoWriter(filename, codec, fps, resolution)
    while traker:
        img = helper_recording.makeOne(pyautogui.screenshot())
        img=cv2.resize(img, resolution)
        frame = np.array(img)
        out.write(frame)
        # if the user clicks q, it exits
    out.release()
    print("stop recording thread")

