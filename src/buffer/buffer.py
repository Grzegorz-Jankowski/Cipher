from dataclasses import asdict
from .text import Text
from typing import List


class Buffer:
    memory: List = []

    @staticmethod
    def show_buffer() -> None:
        for idx, item in enumerate(Buffer.memory, start=1):
            print(f"{idx}. {item}")

    def add(self, new_text: Text) -> None:
        self.memory.append(new_text)

    @staticmethod
    def convert_memory_to_list_of_dicts():
        return [asdict(elem) for elem in Buffer.memory]
