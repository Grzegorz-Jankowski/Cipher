from dataclasses import asdict
from .text import Text
from typing import List


class Buffer:
    memory: List = []

    def show_buffer(self) -> str:
        for idx, item in enumerate(self.memory, start=1):
            return f"{idx}. {item}"

    def add(self, new_text: Text) -> None:
        self.memory.append(new_text)

    @staticmethod
    def convert_memory_to_list_of_dicts():
        return [asdict(elem) for elem in Buffer.memory]
