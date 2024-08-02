import pytest

from mujtaba_charm.utils.sample import color_string, hello


def test_hello():
    assert hello("john") == "hello john!"
    assert hello() == "hello world!"

    with pytest.raises(TypeError) as e:
        hello(2024)
    assert "name should be of string type" in str(e.value)


def test_color_string():
    assert color_string("Hello, world!", "red") == "\033[91mHello, world!\033[0m"
    assert color_string("Hello, world!", "blue") == "\033[94mHello, world!\033[0m"
    assert color_string("Hello, world!", "green") == "\033[92mHello, world!\033[0m"

    with pytest.raises(ValueError) as e:
        color_string("Hello, world!", "yellow")
    assert (
        "Invalid color: yellow. Allowed colors are 'red', 'blue', and 'green'."
        in str(e.value)
    )
