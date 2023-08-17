from buffer import *
from file_handler import *
from encryption import *

"""* zamienię potem dokładnymi funkcjami"""


class Manager:
    def __init__(self):
        self.file_handler = FileHandler()
        self.buffer = Buffer()
        self.encrypting = ROT.Coding()

    def add_new_to_buffer(self):
        return self.buffer.create_new()

    def show_buffer_memory(self):
        return self.buffer.show_buffers()

    def delete_from_buffer_memory(self):
        return self.buffer.delete()

    """Czy teraz rozbijać na zakodowanie i odkodowanie czy mogę mieć w encryption metodę coding, która sama sprawdza
    co ma robić i wtedy w menu bez sensu samemu wybierać co ma robić?"""

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
        file_name = input("Which file do you want to read? ")
        return self.file_handler.read(file_name)

    def save_file(self):
        file_name = input("Which file do you want to save? ")
        file_text = "no skąd to teraz pobrać?"
        return self.file_handler.save_file(file_name, file_text)

    def delete_file(self):
        file_name = input("Which file do you want to delete? ")
        return self.file_handler.delete_file(file_name)
