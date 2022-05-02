from abc import ABC, abstractmethod


class ImageProcessingAbstract(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def extract_channel(self, channel: str):
        pass

    @abstractmethod
    def add_black_border(self, thickness: int):
        pass

    @abstractmethod
    def change_brightness(self, amount: int):
        pass

    @abstractmethod
    def change_contrast(self, amount: int):
        pass
