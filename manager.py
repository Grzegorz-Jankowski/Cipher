from buffer import *
from file_handler import *
from encryption import *

"""* zamienię potem dokładnymi funkcjami"""


class Manager:
    def __init__(self):
        self.file_handler = FileHandler()
        self.buffer = Buffer()
        self.encrypting = Encrypting()

    def add_new_to_buffer(self):
        return self.buffer.create_new()

    def show_buffer_memory(self):
        return self.buffer.show_buffers()

    def delete_from_buffer_memory(self):
        return self.buffer.delete()

    # def encode_rot13(self):
    #     return self.encrypting.encryption_rot13()
    #
    # def encode_rot47(self):
    #     return self.encrypting.encryption_rot47
    #
    # def decode_rot13(self):
    #     return self.encrypting.decrypting_rot13
    #
    # def decode_rot47(self):
    #     return self.encrypting.decrypting_rot47

    def show_files_list(self):
        return self.file_handler.show_files()

    def copy_file_to_buffer(self):
        return self.file_handler.read()

    def save_file(self):
        return self.file_handler.save_file()

    def delete_file(self):
        return self.file_handler.delete_file()
