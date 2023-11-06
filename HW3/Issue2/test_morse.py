import pytest
from morse import decode


@pytest.mark.parametrize(
    "morse_message, expected",
    [
        (".... . .-.. .-.. ---", "HELLO"),  # HELLO без пробелов
        ("-- --- .-. ... .", "MORSE"),  # MORSE без пробелов
        (".- .-.. .--. .... .-", "ALPHA"),  # ALPHA без пробелов
        # Тест с пробелами, ожидается провал
        ("-- --- .-. ... . / -.-. --- -.. .", "MORSE CODE"),
    ],
)
def test_decode(morse_message, expected):
    assert decode(morse_message) == expected
