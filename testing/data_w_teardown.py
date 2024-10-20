import pytest

@pytest.fixture
def prepare_data():
    data = [i for i in range(10)]
    # Return the data with the special keyword
    yield data
    # Clear the data list
    data.clear()
    # Delete the data variable
    del data

def test_elements(prepare_data):
    assert 9 in prepare_data
    assert 10 not in prepare_data
