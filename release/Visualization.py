import pandas as pd
import matplotlib.pyplot as plt
import csv
from pylab import rcParams
import numpy as np
import cv2
import helper_recording as hr
import pyautogui

def BuilderAnalytics(FILENAME):
    rcParams['figure.figsize'] = 16, 5 # редактирование размера изображения в дюймах, нужно как-то автоматом делать

    Number_OF_Keystrokes = {}

    # with open(FILENAME, "r", newline="") as file:
    #     reader = csv.reader(file)
    #     s = 0
    #     for row in reader:
    #
    #         if len(row[1]) > 3:
    #             a = row[1][1:-1].split(',')
    #             for element in a:
    #
    #                 if element not in Number_OF_Keystrokes:
    #                     Number_OF_Keystrokes[element] = 1
    #                 else:
    #                     Number_OF_Keystrokes[element] += 1
    #print(Number_OF_Keystrokes)

    with open('keys.csv', "r", newline="") as file:
        reader = csv.reader(file)
        s = 0
        reader = list(reader)
        for row in reader[1:]:
            element = row[0]
            if element not in Number_OF_Keystrokes:
                Number_OF_Keystrokes[element] = 1
            else:
                Number_OF_Keystrokes[element] += 1

    Number_OF_Keystrokes = pd.Series(Number_OF_Keystrokes)
    plt.title("Количество нажатий клавиш")
    plt.bar(Number_OF_Keystrokes.index, height=Number_OF_Keystrokes, color='b')
    plt_output = plt.gcf()
    # plt.show() # нужно будет убрать
    # plt.draw() # нужно будет убрать
    return plt_output
    # plt_output.savefig('NumberOfKeystrokes.png', dpi=100) #проверка

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
