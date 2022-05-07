import pytest
from app import app


@pytest.mark.get_all
def test_get_all():
    test = app.test_client()
    response = test.get("/")
    assert b'{"name":"Aged Brie"' in response.data
