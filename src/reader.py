import base64
import re
from io import BytesIO

from PIL import Image


def get_image_from_base64(base64_str):
    base64_str = base64_str.replace('\n', '')
    base64_str = re.sub("data:image/[\w]+;base64,", "", base64_str)
    b64decode = base64.b64decode(base64_str)
    b = BytesIO(b64decode)
    return Image.open(b)


def get_image_from_file(path):
    return Image.open(path)
