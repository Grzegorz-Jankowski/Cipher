from manager import Executor, Manager
from buffer import Buffer
import pytest
from unittest.mock import patch, call


class TestExecutor:
    def setup_method(self):
        self.executor = Executor()

    @staticmethod
    def teardown_method():
        Buffer.memory = []

    @patch('builtins.print')
    def test_show_buffer_memory(self, mock_print):
        Buffer.memory = ["apple", "banana", "cherry"]
        self.executor.show_buffer_memory()

        mock_print.assert_has_calls([
            call("1. apple"),
            call("2. banana"),
            call("3. cherry")
        ])

    @pytest.mark.parametrize("rot, word", [("rot13", "nccyr"), ("rot47", "vkkgz")])
    def test_encode(self, rot, word):
        with patch('builtins.input', side_effect=[rot, 'apple']):
            self.executor.encode()
            assert len(Buffer.memory) == 1
            assert Buffer.memory[0].txt == word
            assert Buffer.memory[0].rot_type == rot
            assert Buffer.memory[0].status == "encrypted"

    @pytest.mark.parametrize("rot, word", [("rot13", "nccyr"), ("rot47", "fuuqj")])
    def test_decode(self, rot, word):
        with patch('builtins.input', side_effect=[rot, 'apple']):
            self.executor.decode()
            assert len(Buffer.memory) == 1
            assert Buffer.memory[0].txt == word
            assert Buffer.memory[0].rot_type == rot
            assert Buffer.memory[0].status == "decrypted"

    def test_show_files_list(self):
        """To samo"""
        pass

    def test_ead_and_copy_file_to_buffer(self):
        """To samo"""
        pass

    def test_save_file(self):
        """To samo"""
        pass

    def test_delete_file(self):
        """Tom samo"""
        pass


# class TestManager:
#
#     def test_run(self):
#         """Chyba nie ma sensu"""
#         pass
#
#     @pytest.mark.parametrize("choice, result", [(0, "Invalid number"),
#                              ("asd", "Invalid number"), (999, "Invalid number")])
#     def test_execute_incorrect_input(self, choice, result):
#         execute = Manager.execute
#         # assert execute == result
#         print(execute)
