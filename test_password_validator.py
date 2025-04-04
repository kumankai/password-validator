from password_validator import validate_password

def test_valid_password():
    assert validate_password("Valid1@Pass") == True

### Negative test cases ###
# password length < 8
def test_short_password():
    assert validate_password("abc") == False

# password length > 20
def test_long_password():
    assert validate_password("P@ssw0rdValidator2025!!") == False