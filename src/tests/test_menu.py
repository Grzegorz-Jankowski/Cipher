from menu import Menu
from unittest.mock import patch, call


class TestMenu:

    @patch('builtins.print')
    def test_print_menu_should_show_always_the_same(self, mock_print):
        Menu.show_menu()
        mock_print.assert_has_calls([
            call("Choose any option:\n1. Show buffer memory. \n2. Encode text. \n3. Decode text. \n"
                 "4. Show a list of saved files. \n5. Read file and add to existing list of texts. \n"
                 "6. Save file. \n7. Delete file. \n8. Exit \n")
            ])
