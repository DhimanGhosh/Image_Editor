from abc import ABC
from base.core.image_processing.interface.Image_Processing_Abstract import ImageProcessingAbstract
import numpy as np


class ImageProcessing(ImageProcessingAbstract, ABC):
    def __init__(self, img: np.ndarray):
        super().__init__()
        self.img = img
        self.image_height, self.image_width, self.image_channels = img.shape

    def extract_channel(self, channel) -> np.ndarray:
        """
        This method extracts a specific color channel
        :param channel: 'R' / 'G' / 'B'
        :return: numpy ndarray of the extracted channel of the image
        """
        new_img = self.img.copy()
        if channel.lower() == 'r':
            new_img[:, :, [1, 2]] = 0
        if channel.lower() == 'g':
            new_img[:, :, [0, 2]] = 0
        if channel.lower() == 'b':
            new_img[:, :, [0, 1]] = 0
        return new_img

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
