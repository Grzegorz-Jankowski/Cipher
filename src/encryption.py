from __future__ import annotations
from abc import ABC, abstractmethod

# TODO abstract factory, factory_method
"""Logika metody pod osobną funkcją i potem tylko ją wywołać przy rot13 i 47"""


class ROT(ABC):
    def __init__(self, rot_type):
        self.rot_type = rot_type

    @staticmethod
    def get_rot(rot_type: str) -> ROT13 | ROT47:
        if rot_type == 'rot13':
            return ROT13()
        elif rot_type == 'rot47':
            return ROT47()

    @abstractmethod
    def encrypting(self, message):
        raise NotImplementedError

    @abstractmethod
    def decrypting(self, message):
        raise NotImplementedError


class ROT13(ROT):
    def __init__(self):
        super().__init__(rot_type='rot13')

    def code_13(self):
        """Jak to zmienić, chodzi tylko o znaki +/-"""
        pass

    def encrypting(self, message):
        key = 13
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
        key = 13
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
