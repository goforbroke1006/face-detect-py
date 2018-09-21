from random import randrange

import cv2
import json
import matplotlib.pyplot as plt
import numpy as np

from src.detector import detect
from src.formatter import group_by_context
from src.reader import get_image_from_file

im = get_image_from_file('samples/images/6.jpg')

shapes = detect(im)
background_image = np.array(im)

result = []
for s in shapes:
    result.append(group_by_context(s))

echo json.dumps(result)
