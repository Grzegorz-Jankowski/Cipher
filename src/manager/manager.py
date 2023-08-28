from executor import Executor
from menu.menu import Menu


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
