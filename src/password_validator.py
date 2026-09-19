def is_valid_password(password):
    """Return True if password has at least 8 characters."""
    if not isinstance(password, str):
        raise TypeError("password must be a string")

    return len(password) >= 8


def has_digit(password):
    """Return True if password contains at least one digit."""
    if not isinstance(password, str):
        raise TypeError("password must be a string")

    return any(char.isdigit() for char in password)


def mask_password(password):
    """Return a password represented by asterisks."""
    if not is_valid_password(password):
        raise ValueError("password is not valid")

    return "*" * len(password)