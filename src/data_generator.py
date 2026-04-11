import numpy as np
from src.config import IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS
from src.image_utils import load_image, preprocess
from src.augmentations import augment

def get_shuffled_indices(length):
    return np.random.permutation(length)

def batch_generator(data_dir, image_paths, steering_angles, batch_size, is_training):
    while True:
        i = 0
        images = np.empty([batch_size, IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS])
        steers = np.empty(batch_size)
        
        for index in get_shuffled_indices(image_paths.shape[0]):
            center, left, right = image_paths[index]
            steering_angle = steering_angles[index]
            if is_training and np.random.rand() < 0.7:
                image, steering_angle = augment(data_dir, center, left, right, steering_angle)
            else:
                image = load_image(data_dir, center) 
            images[i] = preprocess(image)
            steers[i] = steering_angle
            i += 1
            if i == batch_size:
                break
        yield images, steers