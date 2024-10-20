import pytest

@pytest.fixture
def prepare_data():
    return [i for i in range(10)]

def test_elements(prepare_data):
    assert 9 in prepare_data
    assert 10 not in prepare_data
