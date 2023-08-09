class OnlyEnglishLetters(Exception):
    def __str__(self):
        return "Please use only English letters!"


class FileDoesExists(Exception):
    def __str__(self):
        return "File name is used. Please try to save using another name."


class WrongChoiceInMenu(Exception):
    def __str__(self):
        return "Please type correct number."


class WrongTypeOfInput(Exception):
    def __str__(self):
        return "Wrong type of data. Please enter a number."
