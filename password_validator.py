def validate_password(password: str) -> bool:
    # Check length of password
    if not (8 <= len(password) <= 20):
        return False
    return True