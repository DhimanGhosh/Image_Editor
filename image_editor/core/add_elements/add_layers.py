from abc import ABC
from image_editor.core.add_elements.interface.add_elements_Abstract import AddElementsAbstract
from image_editor.assets.get_assets import Resources
from image_editor.utils.convert_image import image_to_numpy_array, create_new_image_file
import numpy as np
import os
from PIL import Image, ImageFont, ImageDraw


class AddLayers(AddElementsAbstract, ABC):
    def __init__(self, img: str):
        super().__init__()
        self.img_path = img
        self.img = image_to_numpy_array(img)
        self.image_height, self.image_width, self.image_channels = self.img.shape
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

    def add_text_on_image(self, title_text: str, start_pos: tuple, font_size: int, font_color: tuple) -> str:
        """
        This method adds a specific text at a position of the image
        :param title_text: text to right on the image
        :param start_pos: (x, y) position from where to start writing
        :param font_size: font size of the title text
        :param font_color: **tuple** with RGB color values (R, G, B)
        :return: edited image path
        """
        image = Image.open(self.img_path)
        title_font = ImageFont.truetype(self.res.playfair_font, font_size)
        image_editable = ImageDraw.Draw(image)
        image_editable.text(start_pos, title_text, font_color, font=title_font)

        new_file_name = create_new_image_file(self.img_path)
        image.save(new_file_name)
        return new_file_name
