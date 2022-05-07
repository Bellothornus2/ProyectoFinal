import pytest
from app import app


@pytest.mark.delete_item
def test_delete_item():
    test = app.test_client()
    test.post("/item", json={"name": "hola", "sell_in": 2, "quality": 3})
    result = test.delete("/item", json={"name": "hola", "sell_in": 2, "quality": 3})
    response = test.get("/")
    assert b'{"name":"hola","quality":3,"sell_in":2}' not in response.data
    assert result.status_code == 302
