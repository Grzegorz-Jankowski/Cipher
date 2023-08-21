from typing import Dict
import json
import os
from buffer import Buffer


class FileHandler:

    @staticmethod
    def read(file_name):
        """loading file as buffer and printing."""
        with open(file_name) as json_file:
            data = json.load(json_file)
            print(data)
            Buffer.memory.append(data)

    @staticmethod
    def save_file(file_name, file_text: Dict):
        """Saving buffer as a file."""
        print("Saving file...")

        with open(file_name) as json_file:
            json.dump(file_text, json_file)
        print(f"File {file_name} saved successfully .")

    @staticmethod
    def delete_file(file_name):
        """Deleting file."""
        print("Deleting  file...")
        os.remove(file_name)
        print(f"File {file_name} deleted successfully .")

    @staticmethod
    def show_files():
        """Show list of files."""
        folder = os.listdir("../files")
        print(folder)
