import pytest
from mujtaba_charm.utils.sample import hello

def test_hello():
    assert hello("john") == "hello john!"
    assert hello() == "hello world!"
    assert hello("john") == "hello world!"

    with pytest.raises(TypeError):
        hello(2024)
