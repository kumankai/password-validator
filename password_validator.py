def validate_password(password: str) -> bool:
    # Check length of password
    if not (8 <= len(password) <= 20):
        return False
    
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    special_chars = set("!@#$%^&*0")
    invalid_chars = set("<>{}[]")

    # Keep track of repeating chars
    repeat_count = 0
    last_char = ''

    for char in password:
        # Positive edge cases
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
        
        # Negative edge cases
        if char in invalid_chars:
            return False

        # Repeating characters
        if char == last_char:
            repeat_count += 1
            if repeat_count >= 3:
                return False
        else:
            repeat_count = 1
        last_char = char
    
    return has_lower and has_upper and has_digit and has_special