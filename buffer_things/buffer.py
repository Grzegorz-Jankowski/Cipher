from dataclasses import dataclass


@dataclass
class Buffer:
    text: str = ""
    root_type: str = ""
    status: str = ""
