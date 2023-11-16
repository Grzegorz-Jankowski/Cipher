from buffer import Buffer, Text
from unittest.mock import patch, call


class TestBuffer:

    @staticmethod
    def teardown_method():
        Buffer.memory = []

    @patch('builtins.print')
    def test_show_buffer(self, mock_print):
        Buffer.memory = ["apple", "banana", "cherry"]
        Buffer.show_buffer()

        mock_print.assert_has_calls([
            call("1. apple"),
            call("2. banana"),
            call("3. cherry")
        ])

    @patch('builtins.print')
    def test_show_buffer_empty_memory(self, mock_print):
        Buffer.show_buffer()
        mock_print.assert_not_called()

    def test_add_text_object_to_buffer(self):
        text = Text("abc", "rot13", "encrypted")
        Buffer.add(text)
        assert len(Buffer.memory) == 1
        assert text in Buffer.memory

    def test_convert_memory(self):
        Buffer.memory = [Text("apple", "rot47", "decrypted"), Text("banana", "rot13", "encrypted")]
        result = Buffer.convert_memory_to_list_of_dicts()
        assert result == [{'txt': 'apple', 'rot_type': 'rot47', 'status': 'decrypted'},
                          {'txt': 'banana', 'rot_type': 'rot13', 'status': 'encrypted'}]
