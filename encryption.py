from buffer import Buffer


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

    # """Coś takiego znalazłem, ale nie działa chyba"""
    #
    # key = 47
    # encrypted = []
    #
    # for idx in range(len(message)):
    #     character_idx = ord(message[idx])
    #     if 33 <= character_idx <= 126:
    #         encrypted.append(chr(33 + ((character_idx + 14) % 94)))
    #     else:
    #         encrypted.append(message[idx])
    #
    # return " ".join(encrypted)


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


tekst = "tylko male literki i tyle"
szyfr1 = encrypting_rot13(tekst)
szyfr2 = encrypting_rot47(tekst)
print(szyfr1)
print(szyfr2)
po_hymnie1 = decrypting_rot13(szyfr1)
po_hymnie2 = decrypting_rot13(szyfr2)
print(po_hymnie1)
print(po_hymnie2)


#
# if Buffer.status == "encrypted":
#     print("Encrypting...")
#
#     if Buffer.root_type == "rot13":
#         encrypting_rot13(Buffer.text)
#     else:
#         encrypting_rot47(Buffer.text)
#
# else:
#     print("Decrypting...")
#
#     if Buffer.root_type == "rot13":
#         decrypting_rot13(Buffer.text)
#     else:
#         decrypting_rot47(Buffer.text)


# """stara metoda na kodowanie rot27"""
# def encrypting_rot47(message):
#     key = 47
#     encrypted = ""
#
#     for i in range(len(message)):
#         if ord(message[i]) > 122 - key:
#             encrypted += chr(ord(message[i]) + key - 26)
#         else:
#             encrypted += chr(ord(message[i]) + key)
#
#     return encrypted


# """stara metoda na odkodowanie rot47"""
# def decrypting_rot47(message):
#     key = 47
#     decrypted = ""
#
#     for i in range(len(message)):
#         if ord(message[i]) - key < 97:
#             decrypted += chr(ord(message[i]) - key + 26)
#         else:
#             decrypted += chr(ord(message[i]) - key)
#
#     return decrypted
