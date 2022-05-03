from image_editor.core.image_processing.Image_Processing import ImageProcessing
from image_editor.core.add_elements.add_layers import AddLayers
from image_editor.assets.get_assets import Resources
from image_editor.utils.extract_text_from_image import extract_text_from_image
import numpy as np


res = Resources()
img = res.sample_image


def test_extract_color_channel():
    process = ImageProcessing(img)
    channel = 'R'
    img1 = process.extract_channel(channel)
    new_img = img1[:, :, [1, 2]]
    blank_image_with_red_channel_extracted = np.zeros(img.shape - np.array((0, 0, 1)))
    assert np.array_equal(new_img, blank_image_with_red_channel_extracted)


def test_add_border():
    layer = AddLayers(img)
    border_width = 20
    img1 = layer.add_black_border(border_width)
    difference = (np.array(img1.shape) - np.array(img.shape)).tolist()
    assert tuple(difference) == (border_width * 2, border_width * 2, 0)


def test_add_text():
    layer = AddLayers(img)
    title_text = 'Test Message'
    start_pos = (100, 100)
    font_size = 300
    font_color = (237, 200, 99)
    img1 = layer.add_text_on_image(title_text, start_pos, font_size, font_color)
    text_on_image = extract_text_from_image(img1)
    assert title_text in text_on_image
