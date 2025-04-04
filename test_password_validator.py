import pytest
from password_validator import validate_password

### Positive test cases ###
# Valid password
def test_valid_password():
    assert validate_password("Valid1@Pass") == True

# Min length password (length == 8)
def test_min_length():
    assert validate_password("Vl1dP@ss") == True

# Max length password (length == 20)
def test_max_length():
    assert validate_password("P@sswrdVal1dator2025") == True

### Negative test cases ###
# Password length < 8
def test_short_password():
    assert validate_password("abc") == False

# Password length > 20
def test_long_password():
    assert validate_password("P@ssw0rdValidator2025!!") == False

# Missing uppercase
def test_missing_upper():
    assert validate_password("val1d@pass") == False

# Missing lowercase
def test_missing_lower():
    assert validate_password("VAL1D@PASS") == False

# Missing digit
def test_missing_digit():
    assert validate_password("Valid@Pass") == False

# Missing special character
def test_missing_special():
    assert validate_password("Val1dPass") == False

# Invalid characters (contains invalid character '{')
def test_invalid_characters():
    assert validate_password("Invalid{Pass") == False

# Repeated characters
def test_repeating_characters():
    assert validate_password("Vaaal1d@Pass") == False

# Invalid password type
def test_password_type():
    with pytest.raises(TypeError):
        validate_password(None)
    with pytest.raises(TypeError):
        validate_password(12)