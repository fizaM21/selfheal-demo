from app import load

def test_load():
    assert load("a: 1") == {"a": 1}
