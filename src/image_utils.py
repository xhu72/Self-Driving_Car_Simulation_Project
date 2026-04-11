import cv2, os
from src.config import IMAGE_HEIGHT, IMAGE_WIDTH

def load_image(data_dir, image_file):
    filename = image_file.strip().split('/')[-1].split('\\')[-1]
    filepath = os.path.join(data_dir, 'IMG', filename)
    image = cv2.imread(filepath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def crop(image):
    return image[60:-25, :, :]

def resize(image):
    return cv2.resize(image, (IMAGE_WIDTH, IMAGE_HEIGHT), cv2.INTER_AREA)

def rgb_to_yuv(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2YUV)

def preprocess(image):
    image = crop(image)
    image = resize(image)
    image = rgb_to_yuv(image)
    return image
