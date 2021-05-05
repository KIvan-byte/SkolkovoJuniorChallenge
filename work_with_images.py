import cv2
import pyautogui
import numpy as np
from make_grafics import makes_graph
p = pyautogui.size()


def hconcat_resize(img_list,interpolation=cv2.INTER_CUBIC):
    h_min = min(img.shape[0] for img in img_list)
    im_list_resize = [cv2.resize(img,(int(img.shape[1] * h_min / img.shape[0]),h_min), interpolation=interpolation) for img in img_list]
    return cv2.hconcat(im_list_resize)


def convertToCV2(fig):
    fig.canvas.draw()
    # convert canvas to image
    img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    # img is rgb, convert to opencv's default bgr
    # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, pyautogui.size())
    return img


def makeOne(img):
    image2 = convertToCV2(makes_graph())
    image1 = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    img_h_resize = hconcat_resize([image1, image2])
    return cv2.resize(img_h_resize, p)



