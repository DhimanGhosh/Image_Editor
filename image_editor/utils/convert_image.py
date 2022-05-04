import numpy as np
from matplotlib import pyplot as plt
from glob import glob
import os
from PIL import Image


def image_to_numpy_array(image_path: str) -> np.ndarray:
    img = plt.imread(image_path)
    return img


def numpy_array_to_image(image, image_path: str, file_extension=None) -> str:
    if type(image) == np.ndarray:
        img = Image.fromarray(image)
    else:
        img = Image.open(image)
    new_file_name = create_new_image_file(image_path, file_extension)
    img.save(new_file_name)
    return new_file_name


def create_new_image_file(image_path, file_extension):
    input_file_name = image_path.split(os.sep)[-1]
    if not file_extension:
        file_extension = input_file_name.split('.')[-1]
    new_file_name = input_file_name.split('.')[0] + '_1.' + file_extension
    return new_file_name


def transparent_background(image):
    img = Image.fromarray(image).convert('RGBA')
    data = img.getdata()
    new_data = []
    for item in data:
        if (item[0], item[1], item[2]) == (0, 0, 0):  # Remove black (0, 0, 0) portions of the image
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append(item)
    img.putdata(new_data)
    img.save('temp.png', 'PNG')
    while not glob('temp.png'):
        pass
    return 'temp.png'
