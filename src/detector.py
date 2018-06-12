import numpy as np
import cv2
import dlib
from imutils import face_utils


def detect(pil_image):
    img_input = np.array(pil_image)

    img_gray = cv2.cvtColor(img_input, cv2.COLOR_BGR2GRAY)

    detector = dlib.get_frontal_face_detector()
    rects = detector(img_gray, 0)

    predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')

    res = []
    for r in rects:
        shape = predictor(img_gray, r)
        res.append(face_utils.shape_to_np(shape))

    return res
