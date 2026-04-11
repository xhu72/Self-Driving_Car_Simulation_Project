import cv2
import numpy as np
from src.image_utils import load_image
from src.config import IMAGE_HEIGHT, IMAGE_WIDTH

def select_image(data_dir, center, left, right, steering_angle):
    choice = np.random.choice(3)
    if choice == 0:
        return load_image(data_dir, left), steering_angle + 0.25
    elif choice == 1:
        return load_image(data_dir, right), steering_angle - 0.25
    return load_image(data_dir, center), steering_angle

def random_flip(image, steering_angle):
    if np.random.rand() < 0.5:
        image = cv2.flip(image, 1)
        steering_angle = -steering_angle
    return image, steering_angle

def random_translate(image, steering_angle, range_x=100, range_y=10):
    trans_x = range_x * (np.random.rand() - 0.5)
    trans_y = range_y * (np.random.rand() - 0.5)
    steering_angle += trans_x * 0.002
    trans_m = np.float32([[1, 0, trans_x], [0, 1, trans_y]])
    height, width = image.shape[:2]
    image = cv2.warpAffine(image, trans_m, (width, height))
    return image, steering_angle

def random_shadow(image):
    img = image.copy()
    h, w = img.shape[:2]
    
    x1 = np.random.randint(0, w)
    x2 = np.random.randint(0, w)
    y1 = np.random.randint(0, h//2)
    y2 = np.random.randint(h//2, h)
    points = np.array([[0, y1], [w, y1], [x2, y2], [x1, y2]], dtype=np.int32)
    
    mask = np.zeros((h, w), dtype=np.uint8)
    cv2.fillPoly(mask, [points], 1)
    
    if np.random.rand() < 0.5:
        mask = 1 - mask
    
    s_ratio = np.random.uniform(0.4, 0.7)
    
    hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    hls[:,:,1] = hls[:,:,1] * (1 - mask * (1 - s_ratio))
    return cv2.cvtColor(hls, cv2.COLOR_HLS2RGB)

def random_brightness(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    ratio = 1.0 + 0.4 * (np.random.rand() - 0.5)
    hsv[:,:,2] = hsv[:,:,2] * ratio
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

def augment(data_dir, center, left, right, steering_angle, range_x=100, range_y=10):
    image, steering_angle = select_image(data_dir, center, left, right, steering_angle)
    image, steering_angle = random_flip(image, steering_angle)
    image, steering_angle = random_translate(image, steering_angle, range_x, range_y)
    image = random_shadow(image)
    image = random_brightness(image)
    return image, steering_angle