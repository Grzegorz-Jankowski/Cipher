from __future__ import annotations
from abc import ABC, abstractmethod


class ROT(ABC):
    def __init__(self, rot_type: str, key) -> None:
        self.rot_type = rot_type
        self.key = None

    @staticmethod
    def get_rot(rot_type: str) -> ROT13 | ROT47:
        if rot_type == "rot13":
            return ROT13()
        elif rot_type == "rot47":
            return ROT47()

    def transform(self):
        return self.key

    @abstractmethod
    def encrypting(self, message: str):
        raise NotImplementedError

    @abstractmethod
    def decrypting(self, message: str):
        raise NotImplementedError


class ROT13(ROT):
    def __init__(self):
        super().__init__(rot_type="rot13", key=13)

    def encrypting(self, message):
        # return self.transform(message, 1)
        key = 13
        encrypted = ""
        operation = 1

        for character in message:
            if character.isupper():
                character_idx = ord(character) - ord("A")
                character_shifted = (character_idx + (operation * key)) % 26 + ord(
                    "A"
                )  # character_idx + 13 26 = 39
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

    def decrypting(self, message):
        # return self.transform(message, -1)
        key = 13
        decrypted = ""
        operation = -1

        for character in message:
            if character.isupper():
                character_idx = ord(character) - ord("A")
                character_original_position = (
                    character_idx + (operation * key)
                ) % 26 + ord(
                    "A"
                )  # character_idx + -13 # 26 = 13
                decrypted += chr(character_original_position)

            elif character.islower():
                character_idx = ord(character) - ord("a")
                character_original_position = (
                    character_idx + (operation * key)
                ) % 26 + ord("a")
                decrypted += chr(character_original_position)

            elif character.isdigit():
                character_original_position = (int(character) + (operation * key)) % 10
                decrypted += str(character_original_position)

            else:
                decrypted += character

        return decrypted


class ROT47(ROT):
    def __init__(self):
        super().__init__(rot_type="rot47")

    def code_47(self):
        """Jak to zmienić, chodzi tylko o znaki +/-"""
        pass

    def encrypting(self, message):
        key = 47
        encrypted = ""

        for character in message:
            if character.isupper():
                character_idx = ord(character) - ord("A")
                character_shifted = (character_idx + key) % 26 + ord("A")
                encrypted += chr(character_shifted)

            elif character.islower():
                character_idx = ord(character) - ord("a")
                character_shifted = (character_idx + key) % 26 + ord("a")
                encrypted += chr(character_shifted)

            elif character.isdigit():
                character_new = (int(character) + key) % 10
                encrypted += str(character_new)

            else:
                encrypted += character

        return encrypted

    def decrypting(self, message):
        key = 47
        decrypted = ""

        for character in message:
            if character.isupper():
                character_idx = ord(character) - ord("A")
                character_original_position = (character_idx - key) % 26 + ord("A")
                decrypted += chr(character_original_position)

            elif character.islower():
                character_idx = ord(character) - ord("a")
                character_original_position = (character_idx - key) % 26 + ord("a")
                decrypted += chr(character_original_position)

            elif character.isdigit():
                character_original_position = (int(character) - key) % 10
                decrypted += str(character_original_position)

            else:
                decrypted += character

        return decrypted
