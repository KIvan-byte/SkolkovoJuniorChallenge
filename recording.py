import numpy as np
import pyautogui
import cv2
import work_with_images
import os

traker = True

def stop_recording():
    global traker
    traker = False


def start_recording(name):
    global count
    print("start recording thread")
    while os.path.isfile(f"Videos/__RECORDING_{name}__.avi"):
        name += 1
    p = pyautogui.size()
    resolution = (p[0], p[1]//2)

    codec = cv2.VideoWriter_fourcc(*"XVID")
    filename = f"Videos/__RECORDING_{name}__.avi"

    fps = 12
    out = cv2.VideoWriter(filename, codec, fps, resolution)
    while traker:
        screenshot = pyautogui.screenshot()
        img = work_with_images.makeOne(screenshot)
        img = cv2.resize(img, resolution)
        frame = np.array(img)
        for _ in range(3):
            out.write(frame)
    out.release()
    print("stop recording thread")




