from __future__ import annotations
from buffer import Buffer


# TODO abstract factory, factory_method


class ROT:

    def coding(self, buffer):
        if buffer.status == "encrypted":
            print("Encrypting...")

            if buffer.root_type == "rot13":
                ROT13.encrypting(buffer.text)
            else:
                ROT47.encrypting(buffer.text)

        else:
            print("Decrypting...")

            if buffer.root_type == "rot13":
                ROT13.decrypting(buffer.text)
            else:
                ROT47.decrypting(buffer.text)

    def encrypting(self, message):
        raise NotImplementedError

    def decrypting(self, message):
        raise NotImplementedError


class ROT13(ROT):
    def __init__(self):
        super().__init__(self, root_type="root13")

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
        super().__init__(self, root_type="root47")

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
