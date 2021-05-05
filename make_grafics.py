import pandas as pd
from readCSV import readKeyloggerCSV, readAudioCSV, readMouseGrafCSV
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



def ax1_set(ax1):
    Number_OF_Keystrokes = readAudioCSV('CSV_files/audio.csv')
    time = [i for i in range(len(list(Number_OF_Keystrokes)))]
    num = [float(Number_OF_Keystrokes[el]) for el in Number_OF_Keystrokes]
    num.reverse()
    num = num[:100]
    num.reverse()
    ax1.plot(time[:len(num)], num, color='b')

def ax2_set(ax2):
    keys = readKeyloggerCSV('CSV_files/keys.csv')
    pd_keys = pd.Series(keys)
    ax2.bar(pd_keys.index, height=pd_keys, color='r')

def ax3_set(ax3):
    mt = readMouseGrafCSV('CSV_files/mousegraf.csv')
    time = [i for i in range(len(list(mt)))]
    num = [float(mt[el]) for el in mt]
    num.reverse()
    num = num[:100]
    num.reverse()
    ax3.plot(time[:len(num)], num, color='b')

#  Создаем "Figure" и "Axes":
def makes_graph():
    plt.close('all')
    fig = plt.figure()
    fig.subplots_adjust(wspace=0, hspace=0.5)

    ax_1 = fig.add_subplot(3, 1, 1)
    ax_2 = fig.add_subplot(3, 1, 2)
    ax_3 = fig.add_subplot(3, 1, 3)

    #  Методы, отображающие данные:
    ax1_set(ax_1)
    ax2_set(ax_2)
    ax3_set(ax_3)

    #  Добавление заголовков:
    ax_1.set(title='Audio')
    ax_2.set(title='Кeys')
    ax_3.set(title='Pick moments')
    return fig
