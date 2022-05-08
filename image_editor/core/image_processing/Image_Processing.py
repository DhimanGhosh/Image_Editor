from abc import ABC
from image_editor.core.image_processing.interface.Image_Processing_Abstract import ImageProcessingAbstract
from image_editor.utils.convert_image import image_to_numpy_array, numpy_array_to_image, transparent_background, cv_to_image
import image_editor as ie
import numpy as np
import cv2 as cv


class ImageProcessing(ImageProcessingAbstract, ABC):
    def __init__(self, img: str):
        super().__init__()
        self.img_path = img
        self.img = image_to_numpy_array(img)
        self.image_height, self.image_width, self.image_channels = self.img.shape

    def extract_channel(self, channel: int) -> str:
        """
        This method extracts a specific color channel
        :param channel:
            - image_editor.RED_CHANNEL
            - image_editor.GREEN_CHANNEL
            - image_editor.BLUE_CHANNEL
        :return: path for extracted channel of the image
        """
        new_img = self.img.copy()
        if channel == ie.RED_CHANNEL:
            new_img[:, :, [1, 2]] = 0
        if channel == ie.GREEN_CHANNEL:
            new_img[:, :, [0, 2]] = 0
        if channel == ie.BLUE_CHANNEL:
            new_img[:, :, [0, 1]] = 0
        return numpy_array_to_image(image_array=new_img, image_path=self.img_path)

    def crop_image(self, **kwargs) -> str:
        """
        This method crops an image by dimensions provided
        :param kwargs: arguments to crop the image to some dimension with some aspect ratio
        :return: cropped image path
        """
        new_img = self.img.copy()
        height, width = self.img.shape[:2]
        file_extension = None
        aspect_ratio = kwargs.get('aspect_ratio', ie.CROP_CUSTOM)
        if aspect_ratio == ie.CROP_CUSTOM:
            left, top, right, bottom = kwargs.get('dimension', (0, 0, 0, 0))
            right = width - right
            bottom = height - bottom
            new_img = new_img[top:bottom, left:right, :]
        elif aspect_ratio == ie.CROP_1_1:
            shift = kwargs.get('shift', 0)
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
        elif aspect_ratio == ie.CROP_CIRCLE:
            center = kwargs.get('center', None)
            radius = kwargs.get('radius', None)
            mask = self.__create_circular_mask(height, width, center, radius)
            new_img[~mask] = 0
            new_img = transparent_background(new_img)
            file_extension = 'png'
        new_img_path = numpy_array_to_image(image_array=new_img, image_path=self.img_path, file_extension=file_extension)
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

    def scale_image(self, **kwargs) -> str:
        """
        This method up scales / down scales an image by dimensions provided
        :param kwargs: arguments to scale the image to some dimension
        :return: scaled image path
        """
        img = cv.imread(self.img_path, cv.IMREAD_COLOR)
        scale_amount = abs(float(kwargs.get('amount', '1')))

        if scale_amount >= 1:  # upscale
            img = cv.resize(img, None, fx=scale_amount, fy=scale_amount, interpolation=cv.INTER_CUBIC)

        elif scale_amount > 0:  # downscale
            img = cv.resize(img, None, fx=scale_amount, fy=scale_amount, interpolation=cv.INTER_AREA)

        return cv_to_image(image_cv=img, image_path=self.img_path)

    def flip_image(self, **kwargs) -> str:
        """
        This method flips image horizontally / vertically based on dimensions provided
        :param kwargs: arguments to flip the image to some dimension
        :return: flipped image path
        """
        img = cv.imread(self.img_path, cv.IMREAD_COLOR)
        flip_direction = kwargs.get('direction', ie.FLIP_HORIZONTAL)

        if flip_direction == ie.FLIP_VERTICAL:
            img = cv.flip(img, 0)
        elif flip_direction == ie.FLIP_HORIZONTAL:
            img = cv.flip(img, 1)
        elif flip_direction == ie.FLIP_VERTICAL_HORIZONTAL:
            img = cv.flip(img, -1)

        return cv_to_image(image_cv=img, image_path=self.img_path)
