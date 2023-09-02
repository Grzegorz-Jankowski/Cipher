from __future__ import annotations
from abc import ABC, abstractmethod


class ROT(ABC):
    def __init__(self, rot_type: str, key: int | None) -> None:
        self.rot_type = rot_type
        self.key = None

    @staticmethod
    def get_rot(rot_type: str) -> ROT13 | ROT47:
        if rot_type == "rot13":
            return ROT13()
        elif rot_type == "rot47":
            return ROT47()

    def transform(self, message: str, operation: int) -> str:
        key = self.key
        encrypted = ""

        for character in message:
            if character.isupper():
                character_idx = ord(character) - ord("A")
                character_shifted = (character_idx + (operation * key)) % 26 + ord("A")
                encrypted += chr(character_shifted)

            elif character.islower():
                character_idx = ord(character) - ord("a")
                character_shifted = (character_idx + (operation * key)) % 26 + ord("a")
                encrypted += chr(character_shifted)

            elif character.isdigit():
                character_new = (int(character) + (operation * key)) % 10
                encrypted += str(character_new)

            else:
                encrypted += character

        return encrypted

    @abstractmethod
    def encrypting(self, message: str):
        raise NotImplementedError

    @abstractmethod
    def decrypting(self, message: str):
        raise NotImplementedError


class ROT13(ROT):
    def __init__(self):
        super().__init__(rot_type="rot13", key=13)

    def encrypting(self, message: str) -> str:
        return self.transform(message, 1)

    def decrypting(self, message: str) -> str:
        return self.transform(message, -1)


class ROT47(ROT):
    def __init__(self):
        super().__init__(rot_type="rot47", key=47)

    def encrypting(self, message: str) -> str:
        return self.transform(message, 1)

    def decrypting(self, message: str) -> str:
        return self.transform(message, -1)
