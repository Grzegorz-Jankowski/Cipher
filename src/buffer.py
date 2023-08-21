from dataclasses import dataclass, asdict
from typing import List


@dataclass
class Text:
    txt: str
    rot_type: str
    status: str


class Buffer:
    memory = []

    @staticmethod
    def get_buffers() -> List[Text]:
        """Get Buffer's memory."""
        return Buffer.memory

    @staticmethod
    def add(new_text: Text) -> None:
        """Adding Text to Buffer's memory"""
        Buffer.memory.append(new_text)

    @staticmethod
    def convert_memory_to_list_of_dicts():
        """Changing memory_list to memory_dict."""
        return [asdict(elem) for elem in Buffer.memory]
