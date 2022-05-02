from abc import ABC, abstractmethod


class AddElementsAbstract(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def add_black_border(self, thickness: int):
        pass

    @abstractmethod
    def add_text_on_image(self, text: str, start_pos: tuple, end_pos: tuple):
        pass
