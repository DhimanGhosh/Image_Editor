from abc import ABC
from image_editor.core.image_processing.interface.Image_Processing_Abstract import ImageProcessingAbstract
from image_editor.utils.convert_image import image_to_numpy_array, create_new_image_file, numpy_array_to_image
import numpy as np
from PIL import Image


class ImageProcessing(ImageProcessingAbstract, ABC):
    def __init__(self, img: str):
        super().__init__()
        self.img_path = img
        self.img = image_to_numpy_array(img)
        self.image_height, self.image_width, self.image_channels = self.img.shape

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

    def crop_image(self, **kwargs) -> str:
        """
        This method crops an image by dimensions provided
        :param kwargs: arguments to crop the image to some dimension with some aspect ratio
        :return: cropped image path
        """
        new_img = self.img.copy()
        height, width, _ = self.img.shape
        if kwargs['aspect_ratio'] == 'custom':
            left, top, right, bottom = kwargs['dimension']
            right = width - right
            bottom = height - bottom
            new_img = new_img[top:bottom, left:right, :]
        elif kwargs['aspect_ratio'] == '1:1':
            shift = kwargs['dimension']
            if width > height:
                if (shift + height) <= height:
                    new_img = new_img[:, shift:(shift + height), :]
                else:
                    new_img = new_img[:, (width - height):, :]
            else:
                if (shift + width) <= height:
                    new_img = new_img[shift:(shift + width), :, :]
                else:
                    new_img = new_img[(height - width):, :, :]
        new_img_path = numpy_array_to_image(image=new_img, image_path=self.img_path)
        return new_img_path
