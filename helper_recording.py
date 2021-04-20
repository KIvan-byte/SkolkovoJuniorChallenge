import cv2
import pyautogui
import numpy as np

p = pyautogui.size()
img1 = cv2.imread('analytics.jpg')
# img2 = cv2.imread('hms_victory.jpg')

def hconcat_resize(img_list,
                   interpolation
                   =cv2.INTER_CUBIC):
    # take minimum hights
    h_min = min(img.shape[0]
                for img in img_list)

    # image resizing
    im_list_resize = [cv2.resize(img,
                                 (int(img.shape[1] * h_min / img.shape[0]),
                                  h_min), interpolation
                                 =interpolation)
                      for img in img_list]

    # return final image
    return cv2.hconcat(im_list_resize)




def makeOne(img):
    img_h_resize = hconcat_resize([cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB), img1])
    return cv2.resize(img_h_resize, p)
    # show the Output image
# cv2.imshow('hconcat_resize.jpg', makeOne(pyautogui.screenshot()))
# cv2.waitKey(0)

