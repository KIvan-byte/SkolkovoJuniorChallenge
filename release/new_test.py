import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
import numpy as np
import cv2
import pyautogui
from readCSV import readKeyloggerCSV


def BuilderAnalytics():
    rcParams['figure.figsize'] = 16, 5 # редактирование размера изображения в дюймах, нужно как-то автоматом делать
    Number_OF_Keystrokes = readKeyloggerCSV('keys.csv')
    Number_OF_Keystrokes = pd.Series(Number_OF_Keystrokes)
    plt.title("Количество нажатий клавиш")
    plt.bar(Number_OF_Keystrokes.index, height=Number_OF_Keystrokes, color='r')
    plt_output = plt.gcf()
    return plt_output



def convertToCV2(fig):
    fig.canvas.draw()
    # convert canvas to image
    img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    # img is rgb, convert to opencv's default bgr
    # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, pyautogui.size())
    return img

#
# if __name__ == '__main__':
#     image = hr.makeOne(convertToCV2(BuilderAnalytics("keys.csv")))
#     cv2.imshow('show.jpg', image)
#     cv2.waitKey(0)
