from pynput.mouse import Listener
import datetime
from readCSV import writeToMouseGraf, writeToCSV
mousetraker = []

def on_move(x, y):
    global mousetraker
    if len(mousetraker) > 1:
        now = datetime.datetime.now()
        x0, y0, x1, y1 = mousetraker[0][0], mousetraker[0][1], mousetraker[1][0], mousetraker[1][1]
        transfer = ((x1-x0)**2+(y1-y0)**2)**0.5
        writeToMouseGraf([now, str(transfer)])
        mousetraker.clear()
    else:
        mousetraker.append((x,y))


def on_click(x, y, button, pressed):
    if pressed:
        now = datetime.datetime.now()
        writeToCSV([now, str(x), str(y), str([button])])


def on_scroll(x, y, dx, dy):
    now = datetime.datetime.now()
    writeToCSV([now,str(x),str(y),str([dx,dy])])


def lst():
    print('mouse started')
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()
