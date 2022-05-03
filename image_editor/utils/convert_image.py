import numpy as np
from matplotlib import pyplot as plt


def image_to_numpy_array(image_path: str) -> np.ndarray:
    img = plt.imread(image_path)
    return img
