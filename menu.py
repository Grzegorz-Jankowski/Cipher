from __future__ import annotations
from exceptions import WrongChoiceInMenu, WrongTypeOfInput


class Executor:
    def oneone(self):
        pass

    def twotwo(self):
        pass

    @staticmethod
    def exit_menu():
        Menu.working = False


class Menu:
    def __init__(self):
        self.executor = Executor()
        self.options = {1: self.executor.oneone, 2: self.executor.twotwo, 9: self.executor.exit_menu}
        self.working = True

    def show_menu(self):
        try:
            choice = int(input("Choose any option:\n1. Oneone \n2. Twotwo \n9. Exit \n"))
        except WrongTypeOfInput as e:
            print(e)
        else:
            self.execute(choice)

    @staticmethod
    def show_error():
        return WrongChoiceInMenu

    def execute(self, choice: int):
        self.options.get(choice, self.show_error)
