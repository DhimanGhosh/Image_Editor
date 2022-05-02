from abc import ABC
from image_editor.core.image_processing.interface.Image_Processing_Abstract import ImageProcessingAbstract
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
