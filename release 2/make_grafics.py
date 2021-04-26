import pandas as pd
from readCSV import readKeyloggerCSV, readAudioCSV
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# import cv2
# from work_with_images import convertToCV2



def ax1_set(ax1):
    Number_OF_Keystrokes = readAudioCSV('audio.csv')
    time = [i for i in range(len(list(Number_OF_Keystrokes)))]
    num = [float(Number_OF_Keystrokes[el]) for el in Number_OF_Keystrokes]
    ax1.plot(time, num, color='b')

def ax2_set(ax2):
    keys = readKeyloggerCSV('keys.csv')
    pd_keys = pd.Series(keys)
    ax2.bar(pd_keys.index, height=pd_keys, color='r')



#  Создаем "Figure" и "Axes":
def makes_graph():
    fig = plt.figure()
    fig.subplots_adjust(wspace=0, hspace=0.5)

    ax_1 = fig.add_subplot(2, 1, 1)
    ax_2 = fig.add_subplot(2, 1, 2)

    #  Методы, отображающие данные:
    ax1_set(ax_1)
    ax2_set(ax_2)

    #  Добавление заголовков:
    ax_1.set(title = 'audio')
    ax_2.set(title = 'keys')

    return fig

# if __name__ == '__main__':
#     image = convertToCV2(makes_graph())
#     cv2.imshow('show.jpg', image)
#     cv2.waitKey(0)