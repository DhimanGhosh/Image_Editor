from image_editor.core.image_processing.Image_Processing import ImageProcessing
from image_editor.core.add_elements.add_layers import AddLayers
from image_editor.assets.get_assets import Resources as res
import numpy as np


def test_extract_color_channel():
    img = res.sample_image
    process = ImageProcessing(img)
    channel = 'R'
    img1 = process.extract_channel(channel)
    new_img = img1[:, :, [1, 2]]
    blank_image_with_red_channel_extracted = np.zeros(img.shape - np.array((0, 0, 1)))
    assert np.array_equal(new_img, blank_image_with_red_channel_extracted)


def test_add_border():
    img = res.sample_image
    layer = AddLayers(img)
    border_width = 20
    img1 = layer.add_black_border(border_width)
    difference = (np.array(img1.shape) - np.array(img.shape)).tolist()
    assert tuple(difference) == (border_width * 2, border_width * 2, 0)
