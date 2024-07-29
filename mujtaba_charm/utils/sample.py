"""
This module contains the hello function & string coloring utility.
"""
from typing import Optional

def hello(name: Optional[str] = "world") -> str:
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


def string_coloring_utility(max_temp: Optional[float], min_temp:Optional[float]) -> None:
    """
    Prints the horizontal string bar chart, based on the maximum temperature
    and minimum temperature of the day.

    Args:
        max_temp (float): It is the maximum temperature of a day.
        min_temp (float): It is the minimum temperature of a day.

    Returns:
        None: The function prints the horizontal string bar chart.

    Raises:
        TypeError: If either max_temp or min_temp is not of type float or int.
        ValueError: If either max_temp or min_temp is None or not greater than 0.

    Example:
        >>> string_coloring_utility(1,6)
        +(blue blue) ++++++(red color) 1C - 6C 

        >>> hello(a,m)
        TypeError: max_temp is str, min_temp is int. Both max_temp and min_temp must be of type float or int.
    """

    if not isinstance(max_temp, (int, float)) or not isinstance(min_temp, (int, float)):
        raise TypeError(
            f"max_temp is {type(max_temp).__name__}, min_temp is {type(min_temp).__name__}. Both max_temp and min_temp must be of type float or int."
            )
    
    max_width = 50

    max_bar_length = int(max_temp * max_width)
    min_bar_length = int(min_temp * max_width)

    max_bar = "+" * max_bar_length
    min_bar = "+" * min_bar_length

    print(
        f"\033[94m{min_bar}\033[91m{max_bar}\033[0m {min_temp:02.0f}C - {max_temp:02.0f}C"
    )
