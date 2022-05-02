from abc import ABC
from image_editor.core.add_elements.interface.add_elements_Abstract import AddElementsAbstract
from image_editor.assets.get_assets import Resources
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageFont, ImageDraw


class AddLayers(AddElementsAbstract, ABC):
    def __init__(self, img: np.ndarray):
        super().__init__()
        self.img = img
        self.image_height, self.image_width, self.image_channels = img.shape
        self.res = Resources()

    def add_black_border(self, thickness=1) -> np.ndarray:
        """
        This method adds a black border on all 4 sides of the image
        :param thickness: **int** value for border thickness
        :return: numpy ndarray of the added border of the image
        """
        black = np.zeros((thickness, self.image_width, self.image_channels), dtype='int')
        new_img = np.vstack((black, self.img, black))
        black_T = np.zeros((self.image_height + thickness * 2, thickness, self.image_channels), dtype='int')
        new_img = np.hstack((black_T, new_img, black_T))
        return new_img

    def add_text_on_image(self, text: str, start_pos: tuple, end_pos: tuple) -> np.ndarray:
        """
        This method adds a specific text at a position of the image
        :param text: text to right on the image
        :param start_pos: (x, y) position from where to start writing
        :param end_pos: (x, y) position to where to stop writing
        :return: numpy ndarray of the added border of the image
        """
        image = plt.imread(self.img)
        image = Image.fromarray(np.uint8(image)).convert('RGB')
        title_font = ImageFont.truetype('playfair/playfair-font.ttf', 200)
        pass
