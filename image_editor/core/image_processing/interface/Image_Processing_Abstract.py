from abc import ABC, abstractmethod


class ImageProcessingAbstract(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def extract_channel(self, channel: str):
        pass

    @abstractmethod
    def crop_image(self, **kwargs):
        pass

    @abstractmethod
    def scale_image(self, **kwargs):
        pass

    @abstractmethod
    def flip_image(self, **kwargs):
        pass
