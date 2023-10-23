from typing import Dict
import json
import os
from buffer import Buffer


class FileHandler:
    FILES_DIR: str = ".\\files"
    DEFAULT_FILE_EXTENSIONS: str = ".json"

    @staticmethod
    def get_full_file_path(file_name: str) -> str:
        return (
            rf"{FileHandler.FILES_DIR}\{file_name}{FileHandler.DEFAULT_FILE_EXTENSIONS}"
        )

    @staticmethod
    def read(file_name: str) -> None:
        path = FileHandler.get_full_file_path(file_name)
        with open(path, "r") as json_file:
            data = json.load(json_file)
            print(data)
            Buffer.memory.append(data)

    @staticmethod
    def save_file(file_name: str, file_text: Dict) -> None:
        path = FileHandler.get_full_file_path(file_name)
        print("Saving file...")

        with open(path, "w+") as json_file:
            json.dump(file_text, json_file)
        print(f"File {file_name} saved successfully .")

    @staticmethod
    def delete_file(file_name: str) -> None:
        path = FileHandler.get_full_file_path(file_name)
        print("Deleting  file...")
        os.remove(path)
        print(f"File {file_name} deleted successfully .")

    @staticmethod
    def show_files():
        folder = os.listdir(FileHandler.FILES_DIR)
        if folder:
            print(folder)
        else:
            print("No files.")
