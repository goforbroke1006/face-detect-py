from random import randrange

import cv2
import matplotlib.pyplot as plt
import numpy as np

from src.detector import detect
from src.formatter import group_by_context
from src.reader import get_image_from_base64, get_image_from_file

# im = get_image_from_base64(
#     open('samples/5.txt', 'r').read()
# )

im = get_image_from_file('samples/images/6.jpg')

shapes = detect(im)
background_image = np.array(im)

for s in shapes:
    s2 = group_by_context(s)
    for ctx, points in s2.iteritems():
        rand_color = (
            randrange(0, 255, 32),
            randrange(0, 255, 32),
            randrange(0, 255, 32),
        )
        for px, py in points:
            cv2.circle(background_image, (px, py), 3, rand_color, -1)
plt.imshow(background_image)
plt.show()

