from exceptions import WrongChoiceInMenu


class Executor:
    def oneone(self):
        pass

    def twotwo(self):
        pass


class Menu:
    def __init__(self):
        self.executor = Executor()
        self.options = {1: self.executor.oneone, 2: self.executor.twotwo}
        self.working = True

    def show_menu(self):
        choice = int(input("Choose any option:\n1. Oneone \n2. Twotwo"))
        self.execute(choice)

    @staticmethod
    def show_error():
        return WrongChoiceInMenu

    def execute(self, choice: int):
        self.options.get(choice, self.show_error())

    def exit(self):
        self.working = False
