import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import dlib
import cv2
from imutils import face_utils

im = Image.open('./images/5.jpg')
img_input = np.array(im)


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./../shape_predictor_68_face_landmarks.dat')
img_gray = cv2.cvtColor(img_input, cv2.COLOR_BGR2GRAY)
rects = detector(img_gray, 0)
if len(rects) == 0:
    exit(0)
shape = predictor(img_gray, rects[0])
shape = face_utils.shape_to_np(shape)

img_tmp = img_input.copy()
index = 0
for x, y in shape:
    if 0 <= index <= 16:
        ff_color = (0, 255, 0) # face contour
    elif 17 <= index <= 21:
        ff_color = (0, 255, 255) # right eyebrow
    elif 22 <= index <= 26:
        ff_color = (255, 0, 0) # left eyebrow
    elif 27 <= index <= 30:
        ff_color = (255, 0, 255) # nose center line
    elif 31 <= index <= 35:
        ff_color = (128, 255, 128) # nose bottom line
    elif 36 <= index <= 41:
        ff_color = (255, 64, 128) # right eye
    elif 42 <= index <= 47:
        ff_color = (128, 64, 255) # left eye
    elif 48 <= index <= 54:
        ff_color = (0, 255, 255) # lips (top line)
    elif 55 <= index <= 59:
        ff_color = (128, 255, 128) # lips (bottom line)
    else:
        ff_color = (255, 255, 0) # lips

    cv2.circle(img_tmp, (x, y), 3, ff_color, -1)
    plt.imshow(img_tmp)

    index = index + 1

plt.show()
