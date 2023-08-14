from manager import Manager


class Menu:
    def __init__(self):
        self.manager = Manager()
        self.options = {
            1: self.manager.add_new_to_buffer(),
            2: self.manager.show_buffer_memory(),
            3: self.manager.delete_from_buffer_memory(),
            # 4: encode13,
            # 5: encode47,
            # 6: decode13,
            # 7: decode47,
            8: self.manager.show_files_list(),
            9: self.manager.copy_file_to_buffer(),
            10: self.manager.save_file(),
            11: self.manager.delete_file(),
            12: self.exit_menu
        }
        self.__working = True

    def show_menu(self):
        choice = int(input("Choose any option:\n1. Add new text to the list. \n2. Show list of texts. \n"
                           "3. Delete text from the list. \n4. Encode using ROT13. \n5, Encode using ROT47. \n"
                           "6. Decode using ROT13. \n7. Decode using ROT47. \n8. Show list of saved files. \n"
                           "9. Read file and add to existing list of texts. \n10. Save file. \n11. Delete file. \n"
                           "12. Exit \n"))
        self.options.get(choice)

    def execute(self, choice: int):
        if choice not in self.options.keys():
            print("Invalid Number")
        else:
            self.options.get(choice)

    def run(self):
        while self.__working:
            self.show_menu()

    def exit_menu(self):
        self.__working = False


"""
Jak ma wyglądać menu?
1. Tworzenie tekstu, działanie na bufferze:
    - nowy
    - sprawdzenie co jest
    - usuwanie
2. Kodowanie
    - zakodowanie tego co w bufferze (args: tekst, rot)
    - odkodowanie tego co w bufferze (args: tekst, rot)
3. FileHandler
    - zapisanie
    - usunięcie
    - lista plików
    - pobranie do buffera
    
9. Exit
"""