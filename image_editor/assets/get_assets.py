import os
import shutil


class Resources:
    # FONTs
    playfair_font = os.path.dirname(os.path.realpath(__file__)) + os.sep + 'fonts' + os.sep + 'PlayfairDisplay-Regular.ttf'

    # Images
    sample_image = os.path.dirname(os.path.realpath(__file__)) + os.sep + 'images' + os.sep + 'sample_image.jpg'

    def __init__(self):
        self.__assets_path = os.path.dirname(os.path.realpath(__file__))

    def get_resource_path(self):
        return self.__assets_path

    def store_in_res(self, file_to_store):
        """
        :param file_to_store: original file location from where to copy in res directory
        """
        file_name = file_to_store.split(os.sep)[-1]
        shutil.copy2(file_to_store, self.__assets_path)
        os.remove(file_to_store)
        return self.__assets_path + os.sep + file_name
