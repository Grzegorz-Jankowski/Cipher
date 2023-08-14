from dataclasses import dataclass
from typing import List


@dataclass
class Text:
    txt: str
    root_type: str
    status: str


@dataclass
class Buffer:
    memory = []

    @staticmethod
    def show_buffers() -> List:
        return Buffer.memory

    def create_new(self, new_text: Text) -> None:
        self.memory.append(new_text)

    def delete(self) -> None:
        position = int(input("Which text should be deleted (please add number)? "))
        self.memory.pop(position-1)
