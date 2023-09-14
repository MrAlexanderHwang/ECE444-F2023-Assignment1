#Below code was generated with ChatGPT

from utils import Utils

# Test the reversed function
def test_reversed():
    assert Utils.reversed(123) == 321
    assert Utils.reversed(0) == 0
    assert Utils.reversed(-456) == -654

# Test the formatter function
def test_formatter():
    assert Utils.formatter(10) == ('0b1010', '0o12')
    assert Utils.formatter(255) == ('0b11111111', '0o377')
    assert Utils.formatter(8) == ('0b1000', '0o10')

# Test reversed function with inputs that are strings, floats, and integers
def test_reversed_with_invalid_input():
    try:
        Utils.reversed("123")
    except ValueError as e:
        assert str(e) == "Input must be an integer"

    try:
        Utils.reversed(12.34)
    except ValueError as e:
        assert str(e) == "Input must be an integer"

# Test formatter function with inputs that are strings, floats, and integers
def test_formatter_with_invalid_input():
    try:
        Utils.formatter("123")
    except ValueError as e:
        assert str(e) == "Input must be an integer"

    try:
        Utils.formatter(12.34)
    except ValueError as e:
        assert str(e) == "Input must be an integer"


# Run the tests
test_reversed()
test_formatter()
test_reversed_with_invalid_input()
test_formatter_with_invalid_input()

print("All tests passed.")
