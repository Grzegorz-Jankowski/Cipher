class OnlyEnglishLetters(Exception):
    def __str__(self):
        return "Please use only English letters!"


class FileDoesExists(Exception):
    def __str__(self):
        return "File name is used. Please try to save using another name."


class WrongChoiceInMenu(Exception):
    def __str__(self):
        return "Please type correct number."
