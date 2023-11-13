import io
import tempfile
from file_handler import FileHandler
from buffer import Buffer
import pytest
import os
from unittest.mock import patch
import json


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
    def test_show_files_should_show_all_files(self, mock_stdout):
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_handler = FileHandler()

            file1_path = os.path.join(tmp_dir, 'file1.json')
            file2_path = os.path.join(tmp_dir, 'file1.json')
            os.makedirs(tmp_dir, exist_ok=True)

            with open(file1_path, 'w') as file1, open(file2_path, 'w') as file2:
                file1.write('random_content1')
                file2.write('random_content2')

            file_handler.show_files(tmp_dir)
            assert len(mock_stdout.getvalue()) == 15

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_info_when_no_files_should_show_info(self, mock_stdout):
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_handler = FileHandler()
            file_handler.show_files(tmp_dir)
            excepted_output = "No files.\n"
            assert mock_stdout.getvalue() == excepted_output

    def test_read_should_show_text_and_save_in_buffer_memory(self):
        with tempfile.TemporaryDirectory() as tmp_dir:

            file1_path = os.path.join(tmp_dir, 'file1.json')
            os.makedirs(tmp_dir, exist_ok=True)

            with open(file1_path, 'w') as file1:
                json.dump({'txt': "asd", 'rot_type': "rot13", 'status': "encrypted"}, file1)

            with patch.object(FileHandler, "get_full_file_path", return_value=file1_path):
                FileHandler.read(file1_path)

            assert Buffer.memory == [{'rot_type': 'rot13', 'status': 'encrypted', 'txt': 'asd'}]

    def test_save_file_should_save_file_text_using_file_name(self):
        with tempfile.TemporaryDirectory() as tmp_dir:

            file1_path = os.path.join(tmp_dir, 'file1.json')
            os.makedirs(tmp_dir, exist_ok=True)

            with patch.object(FileHandler, "get_full_file_path", return_value=file1_path):
                FileHandler.save_file(file1_path, {'rot_type': 'rot13', 'status': 'encrypted', 'txt': 'asd'})

            with open(file1_path, 'r') as file1:
                file_what = json.load(file1)

            assert file_what == {'rot_type': 'rot13', 'status': 'encrypted', 'txt': 'asd'}

    def test_delete_file_should_delete_file_using_file_name(self):
        with tempfile.TemporaryDirectory() as tmp_dir:

            file1_path = os.path.join(tmp_dir, 'file1.json')
            os.makedirs(tmp_dir, exist_ok=True)

            with open(file1_path, 'w') as file1:
                json.dump({'txt': "asd", 'rot_type': "rot13", 'status': "encrypted"}, file1)

            with patch.object(FileHandler, "get_full_file_path", return_value=file1_path):
                FileHandler.delete_file(file1_path)

            is_file = os.path.isfile(tmp_dir)
            assert not is_file
