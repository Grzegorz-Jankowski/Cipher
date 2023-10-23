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

    # pytest.parametirze 2/3 przypadki
    def test_ROT13_encrypting(self):
        rot13 = ROT13()
        result = rot13.encrypting("abcd")
        assert result == "nopq"

    def test_encrypting(self):
        pass


    def test_decrypting(self):
        pass
