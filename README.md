# Jacob Angga
# Password Validator

This project provides a simple Python function to validate passwords based on a set of defined security rules. It includes a test suite using `pytest`.

## How to Run

### Run the Tests
Make sure you have Python 3.11+ installed.

1. Install `pytest` (if not already installed):
```bash
pip install pytest
```

2. Run the test file:
```bash
pytest test_password_validator.py
```

Alternatively, if you're using GitHub, tests are automatically run on push using GitHub Actions.

---

## Assumptions and Trade-offs

- **No regular expressions**: The password validation logic avoids the `re` module for clarity and simplicity, using manual checks instead.
- **Allowed special characters**: Only the following are considered valid special characters: `!@#$%^&*()`.
- **Invalid characters**: Angle brackets, square brackets, and curly braces are not allowed.
- **Repeated characters**: More than two of the same character in a row is not allowed.
- **One-pass design**: The function was written to go through the password only once. This led to a small trade-off in modularity, but it helps improve efficiency. Effort was made to keep the logic readable despite being condensed into a single loop.
- **Type checking**: The function raises a `TypeError` if the input is not a string (e.g., passing `None` or an integer).

---

## Project Files
- `password_validator.py`: Contains the `validate_password()` function.
- `test_password_validator.py`: Contains test cases for the validator function using `assert` syntax.

---

## Example Valid Passwords
- `A1b@secure`
- `Z9x!GoodPwd`

## Example Invalid Passwords
- `12345678` (no letters or special character)
- `ABC!@#123` (no lowercase letters)
- `Invaaalid` (more than two repeated characters)
