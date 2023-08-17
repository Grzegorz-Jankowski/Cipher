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
        """Showing texts in buffer's memory."""
        return Buffer.memory

    def create_new(self, new_text: Text) -> None:
        """Creating new text in buffer's memory."""
        self.memory.append(new_text)

    def delete(self) -> None:
        """Deleting from buffer's memory."""
        position = int(input("Which text should be deleted (please add number)? "))
        self.memory.pop(position-1)
