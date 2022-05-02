import os
import shutil


class Resources:
    # FONTs
    playfair = os.path.dirname(os.path.realpath(__file__)) + os.sep + 'fonts' + os.sep + 'playfair-font.ttf'

    # Images
    sample_image = os.path.dirname(os.path.realpath(__file__)) + os.sep + 'images' + os.sep + 'sample_image.jpg'

    def __init__(self):
        self.__assets_path = os.path.dirname(os.path.realpath(__file__))

    def store_in_res(self, file_to_store):
        """
        :param file_to_store: original file location from where to copy in res directory
        """
        shutil.copy2(file_to_store, self.__assets_path)
        os.remove(file_to_store)
