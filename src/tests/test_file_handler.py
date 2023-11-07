import io
import tempfile
from file_handler import FileHandler
from buffer import Buffer
import pytest
import os
from unittest.mock import patch


class TestFileHandler:

    @staticmethod
    def teardown_method():
        Buffer.memory = []

    @pytest.mark.parametrize("file_name, full_path", [("first", ".\\files\\first.json"),
                                                      ("that_file", ".\\files\\that_file.json"),
                                                      ("master11file", ".\\files\\master11file.json")])
    def test_get_full_filename_path_should_show_folder_with_file_name(self, file_name, full_path):
        assert FileHandler.get_full_file_path(file_name) == full_path

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_files(self, mock_stdout):
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_handler = FileHandler()

            file1_path = os.path.join(tmp_dir, 'file1.txt')
            file2_path = os.path.join(tmp_dir, 'file1.txt')
            os.makedirs(tmp_dir, exist_ok=True)

            with open(file1_path, 'w') as file1, open(file2_path, 'w') as file2:
                file1.write('random_content1')
                file2.write('random_content2')

            file_handler.show_files(tmp_dir)
            assert len(mock_stdout.getvalue()) == 14

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_info_when_no_files(self, mock_stdout):
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_handler = FileHandler()
            file_handler.show_files(tmp_dir)
            excepted_output = "No files.\n"
            assert mock_stdout.getvalue() == excepted_output
