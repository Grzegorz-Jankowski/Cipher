from __future__ import annotations
from buffer import Buffer, Text
from encryption import ROT
from file_handler import FileHandler
from menu import Menu


class Executor:
    def __init__(self):
        self.buffer = Buffer()
        self.file_handler = FileHandler()

    def show_buffer_memory(self):
        self.buffer.show_buffer()

    def encode(self):
        user_choice = input("Encode using rot13 or rot47: ")
        rot = ROT.get_rot(user_choice)
        text_to_encode = input("Add your text: ")
        encrypted_text = rot.encrypting(text_to_encode)
        self.buffer.memory.append(Text(encrypted_text, rot.rot_type, "encrypted"))

    def decode(self):
        user_choice = input("Decode using rot13 or rot47? ")
        rot = ROT.get_rot(user_choice)
        text_to_decode = input("Add your text: ")
        decrypted_text = rot.decrypting(text_to_decode)
        self.buffer.memory.append(Text(decrypted_text, rot.rot_type, "decrypted"))

    def show_files_list(self):
        return self.file_handler.show_files()

    def read_and_copy_file_to_buffer(self):
        file_name = input("Which file do you want to read? ")
        return self.file_handler.read(file_name)

    def save_file(self):
        text_to_save = self.buffer.convert_memory_to_list_of_dicts()
        file_name = input("Which file do you want to save? ")
        return self.file_handler.save_file(file_name, text_to_save)

    def delete_file(self):
        file_name = input("Which file do you want to delete? ")
        return self.file_handler.delete_file(file_name)

    @staticmethod
    def exit_menu():
        Manager.__working = False


class Manager:
    def __init__(self):
        self.executor = Executor()
        self.menu = Menu()
        self.options = {
            1: self.executor.show_buffer_memory,
            2: self.executor.encode,
            3: self.executor.decode,
            4: self.executor.show_files_list,
            5: self.executor.read_and_copy_file_to_buffer,
            6: self.executor.save_file,
            7: self.executor.delete_file,
            8: self.executor.exit_menu,
        }
        self.__working = True

    def run(self):
        while self.__working:
            self.menu.show_menu()
            self.execute()

    def execute(self):
        choice = int(input())
        if choice not in self.options.keys():
            print("Invalid number")
        else:
            self.options.get(choice)()
