from encryption import ROT, ROT13, ROT47
import pytest


class TestRot:
    def test_get_rot_returns_correct_object_for_rot13_string(self):
        result = ROT.get_rot("rot13")
        assert isinstance(result, ROT13)

    def test_get_rot_returns_correct_object_for_rot47_string(self):
        result = ROT.get_rot("rot47")
        assert isinstance(result, ROT47)

    def test_get_rot_when_string_is_incorrect(self):
        result = ROT.get_rot("asd")
        assert not result

    @pytest.mark.parametrize("message, result", [("abcd", "nopq"), ("1234", "4567"), ("uhbx", "huok")])
    def test_rot13_encrypting(self, message, result):
        rot13 = ROT13()
        my_function = rot13.encrypting
        assert my_function(message) == result

    @pytest.mark.parametrize("message, result", [("abcd", "vwxy"), ("1234", "8901"), ("uhbx", "pcws")])
    def test_rot47_encrypting(self, message, result):
        rot47 = ROT47()
        my_function = rot47.encrypting
        assert my_function(message) == result

    @pytest.mark.parametrize("message, result", [("abcd", "nopq"), ("1234", "8901"), ("uhbx", "huok")])
    def test_rot13_decrypting(self, message, result):
        rot13 = ROT13()
        my_function = rot13.decrypting
        assert my_function(message) == result

    @pytest.mark.parametrize("message, result", [("abcd", "fghi"), ("1234", "4567"), ("uhbx", "zmgc")])
    def test_rot47_decrypting(self, message, result):
        rot47 = ROT47()
        my_function = rot47.decrypting
        assert my_function(message) == result
