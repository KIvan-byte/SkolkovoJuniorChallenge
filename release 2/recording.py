import pyautogui
import cv2
import numpy as np
import work_with_images

traker = True


def stop_recording():
    global traker
    traker = False


def start_recording():
    print("start recording thread")
    p = pyautogui.size()
    s=0
    resolution = (p[0], p[1]//2)
    codec = cv2.VideoWriter_fourcc(*"XVID")
    filename = "__RECORDING__.avi"
    fps = 4.0
    out = cv2.VideoWriter(filename, codec, fps, resolution)
    while traker:
        img = work_with_images.makeOne(pyautogui.screenshot())
        img = cv2.resize(img, resolution)
        frame = np.array(img)
        s+=1
        out.write(frame)

    out.release()
    print(f"количество кадров {s}")
    print("stop recording thread")
