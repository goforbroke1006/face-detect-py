import base64
import os
import re
import sys
from io import BytesIO

from PIL import Image

# if len(sys.argv) == 1:
#     raise Exception("usage: %s <IMAGE_IN_BASE_64|PATH_TO_IMAGE_ON_HOST>" % os.path.basename(__file__))

# image = sys.argv[1]
# image = sys.stdin.read()
from src.reader import get_image_from_base64

# demo = open('samples/5.txt', 'r')
# image = demo.read().replace('\n', '')
#
# # data = {'img': image}
# image = re.sub("data:image/[\w]+;base64,", "", image)
# b64decode = base64.b64decode(image)
# b = BytesIO(b64decode)
im = get_image_from_base64(
    open('samples/5.txt', 'r').read()
)

im.show()
