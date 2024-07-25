import pytest
from mujtaba_charm.utils.sample import hello

def test_hello():
    assert hello("john") == "hello john!"
    assert hello() == "hello world!"
    assert hello(123)

    with pytest.raises(TypeError) as e:
        hello(2024)
    assert "name should be of string type" in str(e.value)
