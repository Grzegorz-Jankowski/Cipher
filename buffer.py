from dataclasses import dataclass


@dataclass
class Buffer:
    text: str = ""
    root_type: str = ""
    status: str = ""


class EncryptedBuffer(Buffer):
    text: str = ""
    root_type: str = ""
    status: str = "encrypted"


class DecryptedBuffer(Buffer):
    text: str = ""
    root_type: str = ""
    status: str = "decrypted"
