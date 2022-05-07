import pytest
from app import app


@pytest.mark.create_alcohol
def test_add_item():
    test = app.test_client()
    result = test.post("/item", json={"name": "hola", "sell_in": 2, "quality": 3})
    response = test.get("/")
    assert b'{"name":"hola","quality":3,"sell_in":2}' in response.data
    assert result.status_code == 302
    test.delete("/item", json={"name": "hola", "sell_in": 2, "quality": 3})
