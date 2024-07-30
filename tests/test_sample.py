import pytest

from mujtaba_charm.utils.sample import hello, string_coloring_utility


def test_hello():
    assert hello("john") == "hello john!"
    assert hello() == "hello world!"

    with pytest.raises(TypeError) as e:
        hello(2024)
    assert "name should be of string type" in str(e.value)


# ToDo: Have to insert test cases
# def test_string_coloring_utility():
