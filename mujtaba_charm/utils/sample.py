"""
This module contains the hello function.
"""

def hello(name="world"):
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
    """

    if not isinstance(name, str):
        raise TypeError(f" {type(name).__name__} is not allowed, name should be of string type")

    return f"hello {name}!"
