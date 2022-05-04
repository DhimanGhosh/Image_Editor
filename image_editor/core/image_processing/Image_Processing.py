from abc import ABC
from image_editor.core.image_processing.interface.Image_Processing_Abstract import ImageProcessingAbstract
from image_editor.utils.convert_image import image_to_numpy_array, numpy_array_to_image, transparent_background
from glob import glob
import numpy as np
import os


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
        height, width = self.img.shape[:2]
        file_extension = None
        if kwargs.get('aspect_ratio', 'custom') == 'custom':
            left, top, right, bottom = kwargs.get('dimension', (0, 0, 0, 0))
            right = width - right
            bottom = height - bottom
            new_img = new_img[top:bottom, left:right, :]
        elif kwargs.get('aspect_ratio', '1:1') == '1:1':
            shift = kwargs.get('dimension', 0)
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
        elif kwargs.get('aspect_ratio', 'circle') == 'circle':
            center = kwargs.get('center', None)
            radius = kwargs.get('radius', None)
            mask = self.__create_circular_mask(height, width, center, radius)
            new_img[~mask] = 0
            new_img = transparent_background(new_img)
            file_extension = 'png'
        new_img_path = numpy_array_to_image(image=new_img, image_path=self.img_path, file_extension=file_extension)
        if glob('temp.png'):
            os.remove('temp.png')
        return new_img_path

    def __create_circular_mask(self, height, width, center=None, radius=None):
        if center is None:  # use the middle of the image
            center = (width // 2, height // 2)
        if radius is None:  # use the smallest distance between the center and image walls
            radius = min(center[0], center[1], width - center[0], height - center[1])

        Y, X = np.ogrid[:height, :width]
        dist_from_center = np.sqrt((X - center[0]) ** 2 + (Y - center[1]) ** 2)

        mask = dist_from_center <= radius
        return mask
