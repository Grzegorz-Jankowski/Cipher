from manager import Executor, Manager
import pytest
from unittest.mock import patch, call


class TestExecutor:

    @staticmethod
    def teardown_method():
        Buffer.memory = []

    @patch('builtins.print')
    def test_show_buffer_memory(self, mock_print):
        Buffer.memory = ["apple", "banana", "cherry"]
        Executor.show_buffer_memory()

        mock_print.assert_has_calls([
            call("1. apple"),
            call("2. banana"),
            call("3. cherry")
        ])

    def test_encode(self):
        """To samo"""
        pass

    def test_decode(self):
        """To samo"""
        pass

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
