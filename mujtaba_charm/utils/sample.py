"""
This module contains the hello function & string coloring utility.
"""

from typing import Literal


def hello(name="world") -> str:
    """
    Returns a string greeting the name entered as parameter. If no name
    provided, it greets the world.

    Args:
        name (str, optional): The name that is greeted by the function. Default parameter is "world".

    Returns:
        str: A string that greets the user.

    Raises:
        TypeError: If the argument is not of string type.

    Example:
        >>> hello("john")
        'hello john!'

        >>> hello()
        'hello world!'

        >>> hello(2024)
        TypeError: int is not allowed, name should be of string type
    """

    if not isinstance(name, str):
        raise TypeError(f" {type(name).__name__} is not allowed, name should be of string type")

    return f"hello {name}!"


def color_string(text: str, color: Literal["red", "blue", "green"]) -> str:
    """
    Returns the input string in the specified color.

    Args:
        text (str): The string to be colored.
        color (str): The color to apply to the string. Allowed values are 'red', 'blue', and 'green'.

    Returns:
        str: The colored string.

    Raises:
        ValueError: If the specified color is not 'red', 'blue', or 'green'.

    Example:
        >>> color_string("Hello, world!", "red")
        '\033[91mHello, world!\033[0m'

        >>> color_string("Hello, world!", "blue")
        '\033[94mHello, world!\033[0m'
    """
    color_codes = {"red": "\033[91m", "blue": "\033[94m", "green": "\033[92m"}

    reset_code = "\033[0m"
    color = color.lower()
    if color not in color_codes:
        raise ValueError(f"Invalid color: {color}. Allowed colors are 'red', 'blue', and 'green'.")

    return f"{color_codes[color]}{text}{reset_code}"
