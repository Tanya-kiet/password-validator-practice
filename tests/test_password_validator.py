import pytest

from src.password_validator import (
    is_valid_password,
    has_digit,
    mask_password,
)


def test_valid_password():
    assert is_valid_password("password123") == True


def test_invalid_short_password():
    assert is_valid_password("abc") == False


def test_password_type_error():
    with pytest.raises(TypeError):
        is_valid_password(12345)


# def test_mask_password():
#     password = "password123"
#     result = mask_password(password)
#     assert result == "***********"