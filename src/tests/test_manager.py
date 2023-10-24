from manager import Executor, Manager
import pytest


class TestExecutor:

    def test_show_buffer_memory(self):
        """Już otestowane w buffer, czy coś tu jeszcze dodać?"""
        pass

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


class TestManager:

    def test_run(self):
        """Chyba nie ma sensu"""
        pass

    @pytest.mark.parametrize("choice, result", [(0, "Invalid number"),
                             ("asd", "Invalid number"), (999, "Invalid number")])
    def test_execute_incorrect_input(self, choice, result):
        execute = Manager.execute
        # assert execute == result
        print(execute)
