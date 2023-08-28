from dataclasses import asdict
from text import Text


class Buffer:
    memory = []

    def show_buffer(self):
        for idx, item in enumerate(self.memory, start=1):
            print(f"{idx}. {item}")

    def add(self, new_text: Text) -> None:
        self.memory.append(new_text)

    @staticmethod
    def convert_memory_to_list_of_dicts():
        return [asdict(elem) for elem in Buffer.memory]
