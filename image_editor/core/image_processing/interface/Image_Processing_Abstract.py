from abc import ABC, abstractmethod


class ImageProcessingAbstract(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def extract_channel(self, channel: str):
        pass
