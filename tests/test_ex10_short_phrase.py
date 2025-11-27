import pytest

class TestPhraseLen:

    def test_phrase_len(self):
        print("Пожалуйста, введите любую фразу короче 15 символов")
        short_phrase = input("Set a phrase:")
        assert len(short_phrase) < 15, "Фраза не короче 15 символов"