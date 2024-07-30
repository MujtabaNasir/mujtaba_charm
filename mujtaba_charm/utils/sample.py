"""
This module contains the hello function & string coloring utility.
"""

from typing import Optional


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
        raise TypeError(
            f" {type(name).__name__} is not allowed, name should be of string type"
        )

    return f"hello {name}!"


def string_coloring(min_value, max_value) -> None:
    """
    Prints the horizontal string bar chart, based on the maximum value
    and minimum value provided by the user.

    Args:
        min_value (float): It is the maximum value of the bar chart.
        max_value (float): It is the minimum value of the bar chart.

    Returns:
        None: The function prints the horizontal string bar chart.

    Raises:
        TypeError: If either max_value or min_value is not of type float or int.

    Example:
        >>> string_coloring_utility(1,6)
        +(blue blue) ++++++(red color) 1C - 6C

        >>> hello(a,m)
        TypeError: max_value is str, min_value is int. Both max_value and min_value must be of type float or int.
    """

    if not isinstance(min_value, (int, float)) or not isinstance(
        max_value, (int, float)
    ):
        raise TypeError(
            f"max_temp is {type(min_value).__name__}, min_temp is {type(max_value).__name__}. Both max_temp and min_temp must be of type float or int."
        )

    max_width = 50

    min_bar_length = int(min_value * max_width)
    max_bar_length = int(max_value * max_width)

    min_bar = "+" * min_bar_length
    max_bar = "+" * max_bar_length

    create_bars(min_bar, min_value, max_bar, max_value)


def create_bars(min_bar, min, max_bar, max):
    """
    Prints the horizontal string bar chart based on the provided bar strings
    and their corresponding values.

    Args:
        min_bar (str): The string representation of the minimum value bar.
        min_value (float): The minimum value of the bar chart.
        max_bar (str): The string representation of the maximum value bar.
        max_value (float): The maximum value of the bar chart.

    Returns:
        None: The function prints the horizontal string bar chart.

    Example:
        >>> create_bars("++", 1, "++++++", 6)
        ++ (blue) ++++++ (red) 1C - 6C
    """

    print(f"\033[94m{min_bar}\033[91m{max_bar}\033[0m {min:02.0f}C - {max:02.0f}C")
