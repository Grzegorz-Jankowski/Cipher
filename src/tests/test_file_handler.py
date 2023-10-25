from file_handler import FileHandler
from buffer import Buffer
import json
import pytest


class TestFileHandler:

    @staticmethod
    def teardown_method():
        Buffer.memory = []

    @pytest.mark.parametrize("file_name, full_path", [("first", ".\\files\\first.json"),
                                                      ("that_file", ".\\files\\that_file.json"),
                                                      ("master11file", ".\\files\\master11file.json")])
    def test_get_full_filename_path_should_show_folder_with_file_name(self, file_name, full_path):
        assert FileHandler.get_full_file_path(file_name) == full_path

    @staticmethod
    def test_read_when_file_exists(tmp_path):
        file_content = {"key": "value"}
        temp_file = tmp_path / "tempfile.json"
        with open(temp_file, "w") as file:
            json.dump(file_content, file)

            with patch("file_handler.FileHandler.get_full_file_path", return_value=str(temp_file)):
                FileHandler.read("tempfile.json")

        assert file_content in Buffer.memory

    def test_save_file_but_again_how_to_do_this(self):
        pass

    def test_delete_file(self):
        pass

    def test_show_files(self):
        FileHandler.show_files.folder = ["one.json", "two.jason", "ball.json"]
        result = FileHandler.show_files()
        assert result == ["one.json", "two.jason", "ball.json"]

    # def test_show_files_when_empty(self):
    #     folder = []
    #     assert FileHandler.show_files() == "No files."
