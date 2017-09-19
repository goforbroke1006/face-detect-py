import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import dlib
import cv2
from imutils import face_utils


img_input = np.array(Image.open('./samples/images/2.jpg'))
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')
img_gray = cv2.cvtColor(img_input, cv2.COLOR_BGR2GRAY)
rects = detector(img_gray, 0)
shape = predictor(img_gray, rects[0])
shape = face_utils.shape_to_np(shape)


img_tmp = img_input.copy()
for x, y in shape:
    cv2.circle(img_tmp, (x, y), 1, (0, 0, 255), -1)
plt.imshow(img_tmp)

plt.show()