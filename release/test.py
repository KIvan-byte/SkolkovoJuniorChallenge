import numpy as np
import cv2
import matplotlib.pyplot as plt

fig = plt.figure()


x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

ax = fig.add_subplot(2,1,1)
line1, = ax.plot(x1, y1, 'ko-')        # so that we can update data later
ax.set_title('A tale of 2 subplots')
ax.set_ylabel('Damped oscillation')

ay = fig.add_subplot(2, 1, 2)
ay.plot(x2, y2, 'r.-')
ay.set_xlabel('time (s)')
ay.set_ylabel('Undamped')

for i in range(1000):
    # update data
    line1.set_ydata(np.cos(2 * np.pi * (x1+i*3.14/2) ) * np.exp(-x1) )
    print(type(fig))
    input()
    # redraw the canvas
    fig.canvas.draw()

    # convert canvas to image
    img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    img  = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    # img is rgb, convert to opencv's default bgr
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

    # display image with opencv or any operation you like
    cv2.imshow("plot",img)
    k = cv2.waitKey(33) & 0xFF
    if k == 27:
        break