import numpy as np
from matplotlib import pyplot as plt
import os
from PIL import Image


def image_to_numpy_array(image_path: str) -> np.ndarray:
    img = plt.imread(image_path)
    return img


def numpy_array_to_image(image: np.ndarray, image_path: str) -> str:
    img = Image.fromarray(image)
    new_file_name = create_new_image_file(image_path)
    img.save(new_file_name)
    return new_file_name


def create_new_image_file(image_path):
    input_file_name = image_path.split(os.sep)[-1]
    file_extension = input_file_name.split('.')[-1]
    new_file_name = input_file_name.split('.')[0] + '_1.' + file_extension
    return new_file_name
