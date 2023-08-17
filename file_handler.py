import json
import os
from buffer import Buffer

"""Pliki nie mają nazw, nie wiem gdzie dodać? tzn mają nazwy, ale jak dodaję do buffera to je tracą. Buffer to lista
czy lepiej słownik{name: txt}?"""


class FileHandler:

    @staticmethod
    def read(file_name):
        """loading file as buffer and printing."""
        with open(file_name) as json_file:
            data = json.load(json_file)
            print(data)
            Buffer.memory.append(data)

    @staticmethod
    def save_file(file_name, file_text):
        """Saving buffer as file."""
        print("Saving file...")
        with open(file_name) as json_file:
            json.dump(file_text, json_file)
        print(f"File {file_name} saved successfully .")

    @staticmethod
    def delete_file(file_name):
        """deleting file."""
        print("Deleting  file...")
        os.remove(file_name)
        print(f"File {file_name} deleted successfully .")

    @staticmethod
    def show_files():
        """show list of files."""
        folder = os.listdir("jsons")
        print(folder)
