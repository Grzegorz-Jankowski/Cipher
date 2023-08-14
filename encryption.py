from buffer import Buffer

# TODO abstract factory, factory_method


class Coding:
    def __init__(self):
        pass


class Encrypting(Coding):
    pass


class Decrypting(Coding):
    pass


def encrypting_rot13(message):
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


def encrypting_rot47(message):
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


def decrypting_rot13(message):
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


def decrypting_rot47(message):
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


#
# """Kod sprawdzający działanie szyfrowania"""
# tekst = "I'm blue: Yo, listen up here's a story about a little guy."
# szyfr1 = encrypting_rot13(tekst)
# szyfr2 = encrypting_rot47(tekst)
# print("rot13: " + szyfr1)
# print("rot47: " + szyfr2)
# po_hymnie1 = decrypting_rot13(szyfr1)
# po_hymnie2 = decrypting_rot47(szyfr2)
# print("rot13: " + po_hymnie1)
# print("rot47: " + po_hymnie2)


def coding(buffer):
    if buffer.status == "encrypted":
        print("Encrypting...")

        if buffer.root_type == "rot13":
            encrypting_rot13(buffer.text)
        else:
            encrypting_rot47(buffer.text)

    else:
        print("Decrypting...")

        if buffer.root_type == "rot13":
            decrypting_rot13(buffer.text)
        else:
            decrypting_rot47(buffer.text)
