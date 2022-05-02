from base.core.image_processing.Image_Processing import ImageProcessing
from base.core.add_elements.add_layers import AddLayers
from matplotlib import pyplot as plt
import numpy as np


def test_extract_color_channel(res):
    img = plt.imread(res.sample_image)
    process = ImageProcessing(img)
    channel = 'R'
    img1 = process.extract_channel(channel)
    new_img = img1[:, :, [1, 2]]
    blank_image_with_red_channel_extracted = np.zeros(img.shape - np.array((0, 0, 1)))
    assert np.array_equal(new_img, blank_image_with_red_channel_extracted)


def test_add_border(res):
    img = plt.imread(res.sample_image)
    layer = AddLayers(img)
    border_width = 20
    img1 = layer.add_black_border(border_width)
    difference = (np.array(img1.shape) - np.array(img.shape)).tolist()
    assert tuple(difference) == (border_width*2, border_width*2, 0)
