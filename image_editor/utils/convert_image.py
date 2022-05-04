import numpy as np
from matplotlib import pyplot as plt
from glob import glob
import os
from PIL import Image
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


def image_to_numpy_array(image_path: str) -> np.ndarray:
    img = plt.imread(image_path)
    return img


def numpy_array_to_image(image, image_path: str, file_extension=None) -> str:
    img = Image.fromarray(image)
    dirname, extension = create_new_image_file(image_path, file_extension)
    
    if not os.path.isdir(dirname):
        os.makedirs( dirname)
    
    list_of_files = Path(dirname).glob(f'*.{extension}')
    seq_no = max([0]+[int(Path(fn).stem.split('_')[1])  for fn in list_of_files if '_' in Path(fn).stem])
    new_file_path =dirname + os.sep + f'OPIMG_{seq_no + 1}.{extension}'
    img.save(new_file_path)
    return new_file_path

def create_new_image_file(image_path, file_extension):
    input_file_name = image_path.split(os.sep)[-1]
    if not file_extension:
        file_extension = input_file_name.split('.')[-1]
    return os.getenv('OP_DIR') + os.sep + input_file_name.split('.')[0], file_extension


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
    return np.array(img)